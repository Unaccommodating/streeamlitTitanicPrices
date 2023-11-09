import pandas as pd
import streamlit as st

# Read the CSV file into a DataFrame
df = pd.read_csv("data.csv")

selected_gender = st.radio("Выберите пол:", ['муж', 'жен'])

# Filter the data based on the selected gender
if selected_gender == 'муж':
    gender = 'male'
else:
    gender = 'female'

filtered_data = df[df['Sex'] == gender]

# Find the minimum, maximum, and average ticket fare
min_fare = filtered_data['Fare'].min()
max_fare = filtered_data['Fare'].max()
avg_fare = filtered_data['Fare'].mean()

# Display the results
st.write(f"Пол: {gender}")
st.write(f"Минимальная цена: {min_fare}")
st.write(f"Максимальная цена: {max_fare}")
st.write(f"Среднаяя цена: {avg_fare}")