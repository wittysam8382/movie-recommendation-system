import streamlit as st 
import pickle 
import pandas as pd
import requests
def poster_fetch(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=c38d00516b22d150018a49199baa51bf&&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w185/" + data['poster_path']
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    movies_list = sorted(list(enumerate(similarity[index])), reverse = True, key = lambda x: x[1])
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        #fetch from api
        
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(poster_fetch(movie_id))

    return recommended_movies, recommended_movies_posters
    
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = movies_dict = pickle.load(open('similarity.pkl', 'rb'))
st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'How do you', movies['title'].values
)
if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
    
   