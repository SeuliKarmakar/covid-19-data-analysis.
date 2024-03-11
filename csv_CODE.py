import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
import plotly.express as px 
from plotly.subplots import make_subplots 
from datetime import datetime

#INSERTING THE COVID 19 CSV FILE AND PRINTING THE DATA.
covid_df =pd.read_csv() #ENTER THE PATH LOCATION IN THE ().
covid_df.head()

#INSERTING THE VACCINE CSV FILE AND PRINTING THE DATA.
vaccine_df = pd.read_csv() #ENTER THE PATH LOCATION IN THE ().
vaccine_df.head()

#PRINTING THE DATA OF COVID CSV FILE DATE WISE.
covid_df['Date'] = pd.to_datetime(covid_df['Date'], format = '%Y-%m-%d')

#PRINTING THE DATA OF THE  ACTIVE CASES.
covid_df['Active_Cases'] = covid_df['Confirmed'] (covid_df['Cured'] + covid_df['Deaths']) covid_df.tail()

vaccine_df = pd.read_csv("D:/Chrome Downloads/Covid-India/covid_vaccine_statewise.csv")
statewise = pd.pivot_table(covid_df, values = ["Confirmed", "Deaths", "Cured"], index = "State/UnionTerritory", aggfunc max)
statewise["Recovery Rate"] = statewise["Cured"]*100/statewise["Confirmed"]
statewise["Mortality Rate"] = statewise["Deaths"]*100/statewise["Confirmed"]
statewise statewise.sort_values(by = "Confirmed", ascending = False)
statewise.style.background_gradient(cmap = "cubehelix")



top_10_deaths = covid_df.groupby(by 'State/UnionTerritory').max()[['Deaths', 'Date']].sort_values (by= ['Deaths'], ascending = False).reset_index()

fig = plt.figure(figsize=(18,5))

plt.title("Top 10 states with most Deaths", size = 25)

ax = sns.barplot(data = top_10_deaths.iloc[:12], y = "Deaths", x="State/UnionTerritory", linewidth = 2, edgecolor = 'black')

plt.xlabel("States")
plt.ylabel("Total Death Cases")
plt.show()


ax = sns.lineplot(data = covid_df[covid_df['State/UnionTerritory'].isin(['Maharashtr', 'Karnataka','kerala','Tamil Nadu', 'Uttar Pradesh']),x= 'Date', y = 'Active_Cases', hue = 'State/UnionTerritory'])
ax.set_title("Top 5 Affected States in India", size=16)