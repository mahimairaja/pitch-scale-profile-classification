import pandas as pd
import logging as log

df = pd.ExcelFile('dataset.xlsx', engine='openpyxl',)
log.info("List of sheet names : \n")
log.info(df.sheet_names)

df = pd.read_excel('dataset.xlsx', engine='openpyxl', \
                   sheet_name='key_detection_pcp_data_of_midi_',\
                   header=None)

col_name = [f"feature_{x}" for x in range(1, 13)] + ['label']
df.columns = col_name

df.to_csv('training_data.csv', index=False)
log.info("Done! Saved to training_data.csv")