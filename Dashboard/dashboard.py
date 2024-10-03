import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset (you need to replace the file path accordingly)
day_data = pd.read_csv('all_data.csv')

# Convert 'dteday' to datetime
day_data['dteday'] = pd.to_datetime(day_data['dteday'])

# Title of the dashboard
st.title("Bike Usage Analysis Dashboard")

# Sidebar for user inputs
st.sidebar.header("User Inputs")

# Date range filter
start_date = st.sidebar.date_input("Start Date", day_data['dteday'].min())
end_date = st.sidebar.date_input("End Date", day_data['dteday'].max())

# Filter data by date range
filtered_data = day_data[(day_data['dteday'] >= pd.to_datetime(start_date)) & 
                         (day_data['dteday'] <= pd.to_datetime(end_date))]

# Dropdown menu to select data visualization
visualization_type = st.sidebar.selectbox(
    "Select Visualization Type",
    ["Trend of Bike Usage Over Time", "Bike Usage by Temperature", "Working Day vs Holiday Usage"]
)

# Display selected visualization
if visualization_type == "Trend of Bike Usage Over Time":
    st.subheader("Trend of Total Bike Usage Over Time")
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=filtered_data, x="dteday", y="cnt_day", color="b")
    plt.title("Daily Bike Usage Over Time", fontsize=14)
    plt.xlabel("Date")
    plt.ylabel("Total Users (Casual + Registered)")
    st.pyplot(plt)

elif visualization_type == "Bike Usage by Temperature":
    st.subheader("Bike Usage vs Temperature")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=filtered_data, x="temp_day", y="cnt_day", hue="weathersit_day", palette="coolwarm")
    plt.title("Bike Usage vs Temperature with Weather Conditions", fontsize=14)
    plt.xlabel("Temperature (Normalized)")
    plt.ylabel("Total Users")
    st.pyplot(plt)

elif visualization_type == "Working Day vs Holiday Usage":
    st.subheader("Bike Usage: Working Day vs Non-working Day")
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=filtered_data, x="workingday_day", y="cnt_day", palette="Set3")
    plt.title("Bike Usage on Working Days vs Non-working Days", fontsize=14)
    plt.xlabel("Working Day (0 = No, 1 = Yes)")
    plt.ylabel("Total Users")
    st.pyplot(plt)

# Show some basic statistics
st.sidebar.subheader("Basic Statistics")
st.sidebar.write(f"Total Days Analyzed: {len(filtered_data)}")
st.sidebar.write(f"Average Bike Usage: {filtered_data['cnt_day'].mean():.2f}")

# Footer
st.write("## Thank you for exploring!")
st.write("This dashboard provides insights into bike usage trends.")
