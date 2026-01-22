import streamlit as st
import pandas as pd


st.title("This is streamlit webpage")
st.write("This is about some web page defination..")

name=st.text_input("Enter Your Name")

if name:
    st.write(f"Hi {name}! How are you")

age=st.slider("Select your age:",0,10,2,2)
st.write(f"Your age is: {age}")

choice=["Java","Python","C","Powershell"]
st.selectbox("select your favourite language", choice)


df=pd.DataFrame({
    "Name" : ['Amit'],
    "Country": ['India'],
    "Age": [31]

})

st.write(df)

df.to_csv("Sampledata.csv")

upload_file=st.file_uploader("Upload a .csv file", type="csv")

if upload_file is not None:
    df=pd.read_csv(upload_file)
    st.write(df)