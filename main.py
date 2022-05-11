# a322_electricity_trends.py
# This program uses the pandas module to load a 3-dimensional data sheet into a pandas DataFrame object
# Then it will use the matplotlib module to plot comparative line graphs 

import matplotlib.pyplot as plt
import pandas as pd

# choose countries of interest
my_countries = ['Baltimore', 'Motgomery','Prince George']

# Load in the data with read_csv()
df = pd.read_csv("maryland_population_data.csv", header=0)    # header=0 means there is a header in row 0

# get a list unique countries
unique_countries = df['County'].unique()

# Plot the data on a line graph
for c in unique_countries:
  if c in my_countries:
    
    # match country to one of our we want to look at and get a list of years
    years = df[df['County'] == c]['Year']

    # match country to one of our we want to look at and get a list of electriciy values
    sum_elec = df[df['County'] == c]['Population']

    plt.plot(years, sum_elec, label=c)

  
plt.ylabel('Population')
plt.xlabel('Year')
plt.title('Population of Maryland(million)')
plt.legend()
plt.show()