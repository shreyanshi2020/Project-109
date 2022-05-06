import statistics as st
import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd

data = pd.read_csv("sp.csv")
mean = st.mean(data)
median = st.median(data)
mode = st.mode(data)
stdev = st.stdev(data)
mean = stdev.mean(data)
print(mean)
print(median)
print(mode)
print(stdev)
