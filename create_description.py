import os
import pandas as pd
import openpyxl
import datetime as dt

# Open the file as a pandas dataframe
df = pd.read_excel("At Thrift.xlsx")

date = dt.datetime.now().strftime("%d-%b-%Y")

new_file = open(f"{date}_descriptions.txt", "w")

for index, row in df.iterrows():
    title = f"{row['Brand']} {row['Item']} {row['Size']}" 

    cond = row['Condition']
    size = row['Size']
    mat = row['Fabric']
    care = row['Washability']
    ori = row['Country']
    feat = row['Features']

    desc = f"T{title}\nCondition: {cond}\n\nSize: {size}\nMaterial: {mat}\nCare Instructions: {care}\nMade In: {ori}\nFeatures: {feat}\n\nPlease comment with any questions! Measurements shown in photos.\n\nKeywords: \n"

    new_file.write(f"{desc}\n")


