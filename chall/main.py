from ast import Index
from cProfile import label
from operator import index
from pyexpat import features
import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt



header = st.container()
dataset = st.container()
features= st.container()
model_training = st.container()

with header:
    st.title('STRIVE NUTRITION COMPANY')
    st.markdown('* **Members of Team 0:**')
    st.text('Nagarjuna Ravella')
    st.text('Busayo Afolabi')
    st.text('Abubakr Mamajonov')

    df = pd.read_csv('https://raw.githubusercontent.com/chriswmann/datasets/master/500_Person_Gender_Height_Weight_Index.csv')


with dataset:
    st.header('About Data')
    st.subheader('Information about Height')
    histo = pd.DataFrame(df['Height'].value_counts())
    st.bar_chart(histo)

    st.subheader('Information about Weight')
    histo = pd.DataFrame(df['Weight'].value_counts())
    st.bar_chart(histo)

    st.subheader('Gender')
    Gender = pd.DataFrame(df['Gender'].value_counts())
    st.bar_chart(Gender)
    st.text('There are 500 participants in the data')

    st.subheader('Body Mass Index')
    st.markdown('* **0 means** Extremely Weak')
    st.markdown('* **1 means** Weak')
    st.markdown('* **2 means** Normal')
    st.markdown('* **3 means** Overweight')
    st.markdown('* **4 means** Obesity')
    st.markdown('* **5 means** Extreme Obesity')

    st.subheader('Number of people by BMI')
    index = pd.DataFrame(df['Index'].value_counts())
    st.bar_chart(index)
    


    df_female = df[df.Gender == "Female"]
    st.subheader('Number of female by BMI')
    go = pd.DataFrame(df_female['Index'].value_counts())
    st.bar_chart(go)

    df_male = df[df.Gender == "Male"]
    st.subheader('Number of Male by BMI')
    index = pd.DataFrame(df_male['Index'].value_counts())
    st.bar_chart(index)


    st.subheader('Let us compare BMI')
    fig = px.scatter(df, x = 'Weight', y = 'Height', size='Index',color='Index', hover_name='Index')
    st.write(fig)
    
    
    st.subheader('Continue')
    weight_option = df['Index'].unique().tolist()
    weight = st.multiselect('Choose a number', weight_option)
    df = df[df['Index'].isin(weight)]
    fig = px.scatter(df, x = 'Weight', y = 'Height', size='Index',color='Index', hover_name='Index')
    st.write(fig)



    st.title('Thank you')



