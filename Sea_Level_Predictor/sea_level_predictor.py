import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    plt.scatter(x=df['Year'], y = df['CSIRO Adjusted Sea Level'], label = 'original data')


    # Create first line of best fit
    res = linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
    xF = np.arange(df['Year'].min(), 2051, 1)
    yF = res.intercept + res.slope*xF
    plt.plot(xF, yF, 'r', label='fitted line')



    # Create second line of best fit
    new_df = df[df['Year'] > 1999]
    new_reg = linregress(new_df['Year'], new_df['CSIRO Adjusted Sea Level'])
    new_xF = np.arange(2000, 2051, 1)
    new_yF = new_reg.intercept + new_reg.slope*new_xF
    plt.plot(new_xF, new_yF, 'r', label = 'fitted line')



    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()