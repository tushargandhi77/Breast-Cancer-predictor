import streamlit as st
import numpy as np
import pandas as pd
import pickle

model = pickle.load(open('model.pkl','rb'))

st.title("Breast Cancer Predictor")

s2 = st.number_input("Enter Area Worst")

s3 = st.number_input("Enter Concave Point Mean")

s4 = st.number_input("Enter Radius Worst")

s5 = st.number_input("Enter Perimeter Worst")

s6 = st.number_input("Enter concavity Worst")

s7 = st.number_input("Enter Perimeter mean")

if st.button('Prediction:'):
    query = np.array([s2,s3,s4,s5,s6,s7])
    s = str(model.predict([query]))
    if s == '[0]':
        st.title("NO")
    else:
        st.title("YES")