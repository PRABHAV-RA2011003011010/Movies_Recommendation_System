import pickle
import streamlit as st
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[movie_index])),reverse=True,key = lambda x: x[1])
    recommended_movies=[]
    for i in distances[1:6]:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl','rb'))
st.title('Movie recommender')

recommend_movies_like=st.selectbox('What kind of movies do you like?',movies['title'].values)

if st.button('Recommend'):
    recommendations=recommend(recommend_movies_like)
    for i in recommendations:
        st.write(i)




