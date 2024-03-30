import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import pickle

st.write("""
# Rental Real Estate Calculator

This app calculate the **Rental Real Estate** !
""")

st.sidebar.header('User Input Parameters')

#df = user_input_features()

#st.subheader('User Input parameters')
#st.write(df)
house_price = st.sidebar.slider('House Price', 200000, 2000000, 500000)
month_rent = st.sidebar.slider('Monthly Rent', 1000, 10000, 3000)
down_payment = st.sidebar.slider('Down Payment', 40000, 400000, 100000)
loan_term = st.sidebar.slider('Loan Term in Years', 1, 30, 30)
annual_interest = st.sidebar.slider('Annual Interest', 0.00, 10.00, 5.00)
month_tax = st.sidebar.slider('Monthly Taxes', 0, 1000, 250)
data = {'House Price': house_price,
            'Monthly Rent': month_rent,
            'Down Payment': down_payment,
            'Loan Term in Years': loan_term,
            'Annual Interest': annual_interest,
            'Monthly Taxes': month_tax,}

st.subheader('House Price')
st.write("$", str(house_price))

st.subheader('Down Payment(20%)')
st.write("$", str(down_payment))


principle = house_price - down_payment
st.subheader('Principle')
st.write("$", str(principle))

monthly_rate = annual_interest / 12
rate = monthly_rate + 1
number_payment = loan_term * 12
total_payment = 1 - (rate ** (-number_payment))
month_rate = monthly_rate / total_payment
monthly_mortage = month_rate * principle
st.subheader('Monthly Mortage')
st.write("$", str(total_payment))
st.write("$", str(monthly_mortage))

monthly_rental_value = (month_rent / house_price) * 100
st.subheader('Monthly Rent-To-Value')
st.write(str(monthly_rental_value), "%")

annual_gross = month_rent * 12
st.subheader('Annual Gross Rental')
st.write("$", str(annual_gross))

annual_profit = annual_gross - ((monthly_mortage) + month_tax*12)
st.subheader('Annual Profit')
st.write("$", str(annual_profit))

#pickle.dump(clf, open('Model Iris.pkl','wb'))

# Loading model to compare the results
# clf = pickle.load(open('Model Iris.pkl','rb'))