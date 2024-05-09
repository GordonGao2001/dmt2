import pandas as pd

df = pd.read_csv("data/training_set_VU_DM.csv")
df_hotel = df.drop_duplicates(subset=['prop_id'])
print(1)