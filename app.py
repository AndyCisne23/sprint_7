import pandas as pd
import streamlit as st
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')
st.title('Análisis Exploratorio de Datos de Autos')
st.subheader('Análisis del comportamiento de los odómetros y la influencia de estos con el precio de los autos')
hist_checkbox = st.checkbox('Histograma')
scatter_checkbox = st.checkbox('Gráfico de dispersión')

if hist_checkbox:
    st.write('Histograma: Comportamiento de los odómetros')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

if scatter_checkbox:
    st.write('Gráfico de dispersión: Relación entre odómetro y precio')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)