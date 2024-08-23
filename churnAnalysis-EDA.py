import pandas as pd
import numpy as np  
import seaborn as sns 
import matplotlib.ticker as mtick  
import matplotlib.pyplot as plt

data = pd.read_csv("CustomerChurn.csv")
#print(data.sample(5))
print(data.shape)
