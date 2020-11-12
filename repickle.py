# if df.pkl cannot be read by pandas with python<3.8,
# because it was pickled with protocol=5,
# you can run this to generate a pickle file for use in python>3.8
import pandas as pd

df = pd.read_pickle("df.pkl")

df.to_pickle("df_prot4.pkl", protocol=4)
