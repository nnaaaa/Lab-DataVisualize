# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 21:53:34 2015

@author: nymph
"""


#################################### Read the data ############################
import pandas as pd
from pandas import DataFrame, Series
import seaborn as sns
import numpy as np

''' read_csv()
The read_csv() function in pandas package parse an csv data as a DataFrame data structure. What's the endpoint of the data?
The data structure is able to deal with complex table data whose attributes are of all data types. 
Row names, column names in the dataframe can be used to index data.
'''

data = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data-original", delim_whitespace = True, \
 header=None, names = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model', 'origin', 'car_name'])

data['mpg']
data.mpg
data.iloc[0,:]

print(data.shape)
################################## Enter your code below ######################
import matplotlib.pyplot as plt
import seaborn as sns
#import plotly as py

''' Initial Plotting Parameters'''
plt.rcParams
rcDef = plt.rcParams
plt.rcParams.update(plt.rcParamsDefault)

def question_3():
    '''
    What is the range, mean, and standard deviation of each attribute? Pay attention to potential missing values.
    ''' 

    # fill missing values with mean column values
    data.fillna(data.mean(numeric_only=True), inplace=True)

    # Calculate the range, mean, and standard deviation of each numerical attribute
    summary = pd.DataFrame({
        'Range': data.max(numeric_only=True) - data.min(numeric_only=True),
        'Mean': data.mean(numeric_only=True).round(3),
        'Std': data.std(numeric_only=True).round(3)
    })
    
    # Set the name of the index
    summary.index.name = 'Attribute'
    
    # Save the summary to a file
    summary.to_csv('q3_summary.csv')
    return

def question_6():
    '''
    Plot a scatterplot of year vs. cylinders attributes. Add a small random noise to the values to make
    the scatterplot look nicer. What can you conclude? Do some internet search about the history of car
    industry during 70’s that might explain the results.(Hint: data.mpg + np.random.random(len(data.mpg))
    will add small random noise)
    '''
    
    # Set the figure size
    fig_obj = plt.figure(figsize=(10, 7.5))
    ax = plt.subplot(111)
    
    # Plot a scatterplot of year vs. cylinders attributes
    p = plt.plot(data.model + np.random.random(len(data.model)), data.cylinders, 'o', color='b')
    
    # Set the labels
    plt.xlabel('Year')
    plt.ylabel('Cylinders')
    
    # Save the figure
    plt.savefig('q6_scatter.png',bbox_inches='tight')    
    plt.show()
    return

def question_9():
    '''
    Calculate the pairwise correlation, and draw the heatmap with Matplotlib. Do you see some
    interesting correlation? (Hint: data.iloc[:,0:8].corr(), plt.pcolor() draws the heatmap.)
    '''
    # Calculate the pairwise correlation
    corr = data.iloc[:,0:8].corr()
    
    print(corr)
    # Draw the heatmap with Matplotlib
    fig_obj = plt.figure(figsize=(10, 7.5))
    ax = plt.subplot(111)
    p = plt.pcolor(corr)
    plt.colorbar(p)
   
    # put the major ticks at the middle of each cell
    ax.set_xticks(np.arange(corr.shape[0])+0.5, minor=False)
    ax.set_yticks(np.arange(corr.shape[1])+0.5, minor=False)
    
    # want a more natural, table-like display
    ax.invert_yaxis()
    ax.xaxis.tick_top()
    
    # Set the labels
    column_labels = corr.columns
    row_labels = corr.index
    ax.set_xticklabels(column_labels)
    ax.set_yticklabels(row_labels)
    
    # Rotate the labels
    plt.xticks(rotation=90)
    plt.yticks(rotation=0)
    
    # Save the figure
    plt.savefig('q9_heatmap.png',bbox_inches='tight')
    plt.show()

    return

question_6()