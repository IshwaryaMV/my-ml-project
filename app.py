import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("_content_placement_model.pkl")

# Page configuration
st.set_page_config(
    page_title="Student Placement Prediction",
    page_icon="🎓"
)

st.title("🎓 Student Placement Prediction")
st.write("Enter the student's details to predict placement.")

# Input fields
cgpa = st.number_input(
    "CGPA",
    min_value=0.0,
    max_value=10.0,
    value=8.5,
    step=0.1
)

skills = st.number_input(
    "Number of Skills",
    min_value=0,
    max_value=5,
    value=5,
    step=1
)

projects = st.number_input(
    "Number of Projects",
    min_value=0,
    max_value=2,
    value=1,
    step=1
)

internships = st.number_input(
    "Number of Internships",
    min_value=0,
    max_value=2,
    value=2,
    step=1
)

certifications = st.number_input(
    "Number of Certifications",
    min_value=0,
    max_value=5,
    value=5,
    step=1
)

dsa_score = st.number_input(
    "DSA Score",
    min_value=0,
    max_value=100,
    value=85,
    step=1
)

# Prediction button
if st.button("Predict Placement"):
    new_student = pd.DataFrame([{
        "CGPA": cgpa,
        "Skills": skills,
        "Projects": projects,
        "Internships": internships,
        "Certifications": certifications,
        "DSA_Score": dsa_score
    }])

    prediction = model.predict(new_student)

    if prediction[0] == 1:
        st.success("🎉 Prediction: Placed")
    else:
        st.warning("Prediction: Not Placed")
