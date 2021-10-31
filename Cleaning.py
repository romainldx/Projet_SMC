 
import pandas as pd
import numpy as np
import matplotlib as plt
#desired_width=700
#np.set_printoptions(linewidth=desired_width)
#pd.set_option('display.width', desired_width)
#pd.set_option('display.max_columns',35)
df = pd.read_csv(r"C:\Users\RomanBeatz\Desktop\DS\df.csv", sep=";")
df = df.drop('Unnamed: 0',axis=1)
print(df.head)
