import math , shutil
import numpy as np
import pandas as pd
import tensorflow as tf

pd.options.display.max_rows = 10
pd.options.display.float_format = '{:.1f}'.format

!git clone https://github.com/Science1804/California_housing_model 
os.listdir('California_housing_model')
myfile = 'California_housing_model/california_housing_train.csv'
df = pd.read_csv(myfile,sep=',')
df.head()
df.describe()
