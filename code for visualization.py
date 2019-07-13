
# coding: utf-8

# # 1. creating function for all columns (numerical data) of data set 

# In[ ]:


def graph0(cars):
    import pandas as pd                               #importing packges 
    import numpy as np
    import matplotlib.pyplot as plt                   
    
    plots = pd.read_csv(cars)                        #reading file
    # Histogram                   
    for i in list(plots.columns):                     
        plots.hist(column=i,grid=False,figsize=(10,8))      #ploting the histogram graphs 
        plt.savefig(str(i)+'histogram.png')                 #saving the graphs 
        
    #Boxplot
        plots.boxplot(column=i,grid=False,figsize=(10,8))    #plotting the boxplot graphs
        plt.savefig(str(i)+'boxplot.png')                    #saving the graphs 


# # 2.creating function to plot graphs for specific columns (numerical data) of data set 

# In[ ]:


def graph1(car,t=[1,4,5]):
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    
    plots = pd.read_csv(car)  # reading file in csv 
    for q in t :
        j= plots.columns[q]   # reading corresponding column name
        # Plotting Histogram 
        plots.hist(column=j,grid = False,figsize=(10,8))
        plt.show()
        
        
        # plotting Boxplot
        plots.boxplot(column=j,grid= False,figsize=(10,8))
        plt.show()
    
    


# #  3. Function for ploting the graphs when no column is specified 

# In[ ]:


def graph2(car,t=[]) :
    import pandas as pd
    import numpy as np                           #importing packages 
    import matplotlib.pyplot as plt
    
    plots = pd.read_csv(car)                     #reading the imported file 
    if(t==[]):                                   
        t = list(plots.columns)                  # list of column names
    
    for j in t :
        # Histogram 
        plots.hist(column=j,grid = False,figsize=(10,8))
        plt.show()
        
        
        # Boxplot
        plots.boxplot(column=j,grid= False,figsize=(10,8))
        plt.show()


# # 4.creating function to plot boxplots & histograms for the numerical variables and bar plots for categorical variables.

# In[1]:


def graph3(car,t=[]):
    import pandas as pd
    import numpy as np                    #importing packeges 
    import matplotlib.pyplot as plt
    
    plots = pd.read_csv(car)
    if(t==[]):
        t = list(plots.columns)
    numeric =[]                         
    categorical =[]
    
    # Segregating numerical and categorical data 
    for i in t :
        if(plots[i].dtypes=="object"):    
            categorical.append(i)
        else:
            numeric.append(i)
    # ploting histogram and boxplot for numerical data 
    for j in numeric:
        # Histogram 
        plots.hist(column=j,grid = False,figsize=(10,8))
        plt.show()
        
        
        # Boxplot
        plots.boxplot(column=j,grid= False,figsize=(10,8))
        plt.show()
        
    # ploting bar graph for categorical data 
    for j in categorical:
        #Bargraph
        plots[j].value_counts().plot(kind="bar",figsize=(6,4),color="coral",fontsize=13)
        plt.show()


# # 5.Create an additional argument in the function called "dir" (directory), which will enable the function to export all the image files to  specified folder .

# In[ ]:


def graph4(car,dir_name,t=[]):
    import pandas as pd
    import os                                #importing packeges 
    import matplotlib.pyplot as plt
    
    plots = pd.read_csv(car)
    if(t==[]):
        t = list(plots.columns)
    numeric =[]
    categorical =[]
    
    # Segregating numerical and categorical data
    for j in t :
        if(plots[j].dtypes=="object"):
            categorical.append(j)
        else:
            numeric.append(j)
             
    os.mkdir(dir_name)       # creates new directory 
    os.chdir(dir_name)       # changes directory to given path
    
    # ploting histogram and boxplot for numerical data 
    for j in numeric:
        # Histogram 
        plots.hist(column=j,grid = False,figsize=(10,8))
        plt.savefig(str(j)+'histogram.png')
        plt.show()
        
        
        # Boxplot
        plots.boxplot(column=j,grid= False,figsize=(10,8))
        plt.savefig(str(j)+'boxplot.png')
        plt.show()
        
    # ploting bar graph for categorical data    
    for j in categorical:
        #Bargraph
        plots[j].value_counts().plot(kind="bar",figsize=(6,4),color="coral",fontsize=13)
        plt.savefig(str(j)+'bargraph.png')
        plt.show()

