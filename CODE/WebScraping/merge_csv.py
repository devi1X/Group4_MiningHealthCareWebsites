import pandas as pd

df1 = pd.read_csv('../../DATA/WebScraping_Data/camh_data.csv', index_col=0)
df2 = pd.read_csv('../../DATA/WebScraping_Data/medhelp_data.csv', index_col=0)
df3 = pd.read_csv('../../DATA/WebScraping_Data/patient_data.csv', index_col=0)

merged_df = pd.concat([df1, df2, df3], ignore_index=True)

#merged_df = merged_df.reset_index(drop=True)

merged_df.to_csv('merged_file.csv')

print('Done')