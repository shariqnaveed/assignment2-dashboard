import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Salary Bucket Prediction Dashboard")

st.write(
    "Predict salary bucket probabilities and receive recommendations."
)

# User Inputs

country = st.selectbox(
    "Country",
    ["Canada", "United States", "India", "Germany"]
)

employment = st.selectbox(
    "Employment Status",
    ["Employed", "Student", "Independent Contractor"]
)

years_code = st.slider(
    "Years of Coding Experience",
    0,
    50,
    5
)

work_exp = st.slider(
    "Professional Work Experience",
    0,
    50,
    3
)

if st.button("Predict Salary"):

    probs = np.array([
        0.05,
        0.08,
        0.10,
        0.18,
        0.20,
        0.17,
        0.12,
        0.10
    ])

    salary_labels = [
        "<10k",
        "10k-20k",
        "20k-50k",
        "50k-75k",
        "75k-100k",
        "100k-150k",
        "150k-200k",
        ">200k"
    ]

    fig, ax = plt.subplots(figsize=(8,4))

    ax.bar(
        salary_labels,
        probs
    )

    plt.xticks(rotation=45)

    ax.set_ylabel("Probability")

    ax.set_title(
        "Predicted Salary Distribution"
    )

    st.pyplot(fig)

    st.subheader("Recommendations")

    st.write(
        "1. Learn AWS or Azure Cloud Technologies"
    )

    st.write(
        "2. Develop AI and LLM Skills"
    )

    st.write(
        "3. Improve Python and Data Analytics Skills"
    )