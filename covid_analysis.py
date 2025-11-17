# -----------------------------------------------
# COVID-19 Data Analysis - Fully Self-Contained
# No external CSV/Excel needed
# -----------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os

# -----------------------------
# Step 1: Generate Synthetic Dataset
# -----------------------------

# Create a date range
dates = pd.date_range(start='2022-01-01', periods=100)

# Generate synthetic data for 2 countries: India and USA
data = {
    'date': list(dates)*2,
    'country': ['India']*100 + ['USA']*100,
    'new_cases': np.random.randint(1000, 10000, size=200),
    'total_cases': np.cumsum(np.random.randint(1000, 10000, size=200)),
    'new_deaths': np.random.randint(10, 500, size=200),
    'total_deaths': np.cumsum(np.random.randint(10, 500, size=200)),
    'total_vaccinations': np.cumsum(np.random.randint(5000, 20000, size=200)),
    'people_vaccinated': np.cumsum(np.random.randint(2000, 10000, size=200))
}

covid_df = pd.DataFrame(data)

# -----------------------------
# Step 2: Filter for a Country
# -----------------------------
country_name = 'India'
country_df = covid_df[covid_df['country'] == country_name].copy()

# -----------------------------
# Step 3: Exploratory Data Analysis (EDA)
# -----------------------------

# Create images folder if not exists
os.makedirs("images", exist_ok=True)

# 1. Daily New Cases
plt.figure(figsize=(12,6))
sns.lineplot(data=country_df, x='date', y='new_cases')
plt.title(f"Daily New COVID-19 Cases in {country_name}")
plt.xlabel("Date")
plt.ylabel("New Cases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f"images/daily_new_cases_{country_name}.png")
plt.show()

# 2. Daily New Deaths
plt.figure(figsize=(12,6))
sns.lineplot(data=country_df, x='date', y='new_deaths', color='red')
plt.title(f"Daily New COVID-19 Deaths in {country_name}")
plt.xlabel("Date")
plt.ylabel("New Deaths")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f"images/daily_new_deaths_{country_name}.png")
plt.show()

# 3. Vaccination Progress
plt.figure(figsize=(12,6))
sns.lineplot(data=country_df, x='date', y='total_vaccinations', color='green')
sns.lineplot(data=country_df, x='date', y='people_vaccinated', color='blue')
plt.title(f"COVID-19 Vaccination Progress in {country_name}")
plt.xlabel("Date")
plt.ylabel("Number of People")
plt.legend(['Total Vaccinations','People Vaccinated'])
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f"images/vaccination_progress_{country_name}.png")
plt.show()

# 4. Optional Interactive Plotly Graph
fig = px.line(country_df, x='date', y=['new_cases', 'new_deaths'],
              title=f'COVID-19 Daily Cases and Deaths in {country_name}')
fig.show()

# -----------------------------
# Step 4: Summary Insights
# -----------------------------
print(f"\n----- Summary for {country_name} -----")
print("Total Cases:", country_df['total_cases'].iloc[-1])
print("Total Deaths:", country_df['total_deaths'].iloc[-1])
print("Total Vaccinations:", country_df['total_vaccinations'].iloc[-1])
print("People Vaccinated:", country_df['people_vaccinated'].iloc[-1])

# -----------------------------
# Step 5: Compare Multiple Countries (Optional)
# -----------------------------
# Example: Plot total cases of India vs USA
plt.figure(figsize=(12,6))
sns.lineplot(data=covid_df, x='date', y='total_cases', hue='country')
plt.title("Total COVID-19 Cases: India vs USA")
plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("images/total_cases_comparison.png")
plt.show()
