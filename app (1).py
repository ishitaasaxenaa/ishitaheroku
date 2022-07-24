import streamlit as st
st.set_page_config(page_title = "Ishita's streamlit app")

st.subheader('Hi, I am Ishita')
st.title('App to find whether the given number is odd or even')
x = st.number_input('Enter a number')
if (x).is_integer():
    if x%2==0:st.write("your number is even")
    elif x%2!=0:st.write("your number is odd")
else:st.write("please enter integer number")