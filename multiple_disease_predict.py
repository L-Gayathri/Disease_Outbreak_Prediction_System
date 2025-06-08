# -*- coding: utf-8 -*-
"""
Created on Sun Jun  8 15:08:30 2025
@author: lakka
"""
import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
st.set_page_config(page_title="Health Predictor",
                   layout="wide",
                   page_icon="🧑‍⚕️")

    
# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))
import base64

# Function to convert image to base64
def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Load models
diabetes_model = pickle.load(open('E:/disease outbreak prediction system/Saved Models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('E:/disease outbreak prediction system/Saved Models/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('E:/disease outbreak prediction system/Saved Models/parkinsons_model.sav', 'rb'))

# Sidebar navigation
with st.sidebar:
    selected = option_menu(
        'disease outbreak prediction System',
        ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
        icons=['activity', 'heart', 'person'],
        default_index=0
    )

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')

    bg_image_path = "E:\disease outbreak prediction system\static\diabetes.webp"
    bg_image_base64 = image_to_base64(bg_image_path)

    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url('data:image/jpeg;base64,{bg_image_base64}');
            background-size: cover;
            background-attachment: fixed;
            background-repeat: no-repeat;
        }}
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="diabetes-section">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the Person')

    diab_diagnosis = ''

    if st.button('Diabetes Test Result'):
        try:
            user_input = [float(x) for x in [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]
            diab_prediction = diabetes_model.predict([user_input])
            diab_diagnosis = 'The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic'
        except ValueError:
            diab_diagnosis = "⚠️ Please enter valid numeric values in all fields."

    st.success(diab_diagnosis)
    st.markdown('</div>', unsafe_allow_html=True)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')

    bg_image_path = "E:\disease outbreak prediction system\static\heart_disease.jpg"
    bg_image_base64 = image_to_base64(bg_image_path)

    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url('data:image/jpeg;base64,{bg_image_base64}');
            background-size: cover;
            background-attachment: fixed;
            background-repeat: no-repeat;
        }}
        </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1: age = st.text_input('Age')
    with col2: sex = st.text_input('Sex')
    with col3: cp = st.text_input('Chest Pain types')
    with col1: trestbps = st.text_input('Resting Blood Pressure')
    with col2: chol = st.text_input('Serum Cholestoral in mg/dl')
    with col3: fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    with col1: restecg = st.text_input('Resting Electrocardiographic results')
    with col2: thalach = st.text_input('Maximum Heart Rate achieved')
    with col3: exang = st.text_input('Exercise Induced Angina')
    with col1: oldpeak = st.text_input('ST depression induced by exercise')
    with col2: slope = st.text_input('Slope of the peak exercise ST segment')
    with col3: ca = st.text_input('Major vessels colored by flourosopy')
    with col1: thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    heart_diagnosis = ''

    if st.button('Heart Disease Test Result'):
        try:
            user_input = [float(x) for x in [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
            heart_prediction = heart_disease_model.predict([user_input])
            heart_diagnosis = 'The person is having heart disease' if heart_prediction[0] == 1 else 'The person does not have any heart disease'
        except ValueError:
            heart_diagnosis = "⚠️ Please enter valid numeric values in all fields."

    st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":
    st.title("Parkinson's Prediction using ML")

    bg_image_path = "E:\disease outbreak prediction system\static\parkinsons.webp"
    bg_image_base64 = image_to_base64(bg_image_path)

    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url('data:image/jpeg;base64,{bg_image_base64}');
            background-size: cover;
            background-attachment: fixed;
            background-repeat: no-repeat;
        }}
        </style>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4, col5 = st.columns(5)

    inputs = [
        'MDVP:Fo(Hz)', 'MDVP:Fhi(Hz)', 'MDVP:Flo(Hz)', 'MDVP:Jitter(%)', 'MDVP:Jitter(Abs)',
        'MDVP:RAP', 'MDVP:PPQ', 'Jitter:DDP', 'MDVP:Shimmer', 'MDVP:Shimmer(dB)',
        'Shimmer:APQ3', 'Shimmer:APQ5', 'MDVP:APQ', 'Shimmer:DDA', 'NHR',
        'HNR', 'RPDE', 'DFA', 'spread1', 'spread2', 'D2', 'PPE'
    ]

    user_values = []
    for i, feature in enumerate(inputs):
        col = [col1, col2, col3, col4, col5][i % 5]
        with col:
            val = st.text_input(feature)
            user_values.append(val)

    parkinsons_diagnosis = ''
    if st.button("Parkinson's Test Result"):
        try:
            input_data = [float(x) for x in user_values]
            parkinsons_prediction = parkinsons_model.predict([input_data])
            parkinsons_diagnosis = "The person has Parkinson's disease" if parkinsons_prediction[0] == 1 else "The person does not have Parkinson's disease"
        except ValueError:
            parkinsons_diagnosis = "⚠️ Please enter valid numeric values in all fields."

    st.success(parkinsons_diagnosis)

# Global styling
st.markdown("""
    <style>
    .diabetes-section
    {
     background-color:red;}
    .st-emotion-cache-ocqkz7
    {
     background-color: white;
border-radius: 20px;
padding: 25px;
}
    .st-emotion-cache-qoz3f2 p, .st-emotion-cache-qoz3f2 ol, .st-emotion-cache-qoz3f2 ul, .st-emotion-cache-qoz3f2 dl, .st-emotion-cache-qoz3f2 li {
    font-size: inherit;
    color: black;
    font-weight: bolder;
}
    .st-emotion-cache-1sdpuyj h1, .st-emotion-cache-1sdpuyj h2, .st-emotion-cache-1sdpuyj h3, .st-emotion-cache-1sdpuyj h4, .st-emotion-cache-1sdpuyj h5, .st-emotion-cache-1sdpuyj h6, .st-emotion-cache-1sdpuyj span {
    scroll-margin-top: 3.75rem;
    background-color: #181b56;
    margin: -20px 0px 76px 0px;
    border-radius: 20px;
    text-align: center;
}
    .st-emotion-cache-seewz2 p, .st-emotion-cache-seewz2 ol, .st-emotion-cache-seewz2 ul, .st-emotion-cache-seewz2 dl, .st-emotion-cache-seewz2 li {
    font-size: inherit;
    background-color: #000;
    border-radius: 10px;
}
    .st-emotion-cache-ovf5rk p, .st-emotion-cache-ovf5rk ol, .st-emotion-cache-ovf5rk ul, .st-emotion-cache-ovf5rk dl, .st-emotion-cache-ovf5rk li {
    font-size: inherit;
    background-color: #42c142;
    border-radius: 10px;
    padding: 6px;
}
    </style>
""", unsafe_allow_html=True)
