import streamlit as st
import numpy as np
import joblib

# Load the trained model pipeline
model = joblib.load("customer_churn_pipeline.pkl")

st.title("E-commerce Customer Churn Predictor")

st.markdown("""
Enter customer details to predict the likelihood of churn.
""")

# User inputs
product_price = st.slider("Product Price", 10, 500, 250)
quantity = st.slider("Quantity", 1, 5, 2)
total_purchase = st.slider("Total Purchase Amount", 100, 5500, 2500)
customer_age = st.slider("Customer Age", 18, 70, 35)
returns = st.radio("Has the customer returned items?", ["Yes", "No"])
gender = st.radio("Gender", ["Male", "Female"])
payment_method = st.selectbox("Payment Method", ["Credit Card", "PayPal", "Crypto"])
product_category = st.selectbox("Product Category", ["Clothing", "Electronics", "Home"])

# Convert inputs to model format
returns_val = 1 if returns == "Yes" else 0
gender_male = 1 if gender == "Male" else 0
payment_credit = 1 if payment_method == "Credit Card" else 0
payment_crypto = 1 if payment_method == "Crypto" else 0
payment_paypal = 1 if payment_method == "PayPal" else 0
category_clothing = 1 if product_category == "Clothing" else 0
category_electronics = 1 if product_category == "Electronics" else 0
category_home = 1 if product_category == "Home" else 0

# Create input array for model
input_data = np.array([[product_price, quantity, total_purchase, customer_age,
                        returns_val, customer_age,
                        gender_male,
                        payment_credit, payment_crypto, payment_paypal,
                        category_clothing, category_electronics, category_home]])

if st.button("Predict Churn"):
    result = model.predict(input_data)
    if result[0] == 1:
        st.error("This customer is likely to churn ")
    else:
        st.success("This customer is likely to stay ")
