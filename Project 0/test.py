#%%
import pandas as pd
import altair as alt
import numpy as np
#%%
from IPython.display import Markdown
from IPython.display import display
from tabulate import tabulate

#%%

url = "https://github.com/byuidatascience/data4python4ds/raw/master/data-raw/mpg/mpg.csv"
mpg = pd.read_csv(url)


chart = (alt.Chart(mpg)
  .encode(
    x='displ', 
    y='hwy')
  .mark_circle()
)

chart
# %%
