import pandas as pd
df = pd.read_csv('CarInventory.csv')
# df = pd.read_excel('CarInventory.xlsx')



# 1) Sort Rows According to a column
df = df.sort_values(['Miles'], ascending=False)
df.reset_index(drop=True, inplace=True)


# 2) Create Column [No Conditions]
# df['Age till 2021'] = 21 - df['Mfg Year']

# Create Column [With Conditions]
def condition(row):
    if row['Mfg Year'] >= 0 and row['Mfg Year'] <= 21:
        return 21 - row['Mfg Year']
    else:
        return 21 + (100 - row['Mfg Year'])

df['Age till 2021'] = df.apply(condition, axis=1)



# 3) Rearrange column
df = df[['Car ID','Maker','Model','Model Full Name','Mfg Year','Age till 2021','Miles','Covered?']]

# Rearrange column [List Slicing Method]
# cols = list(df.columns)
# df = df[cols[0:5] + [cols[-1]] + cols[5:7]]


# 4) Conditional changes
df.loc[df['Model Full Name'] == 'Camery', 'Model Full Name'] = 'Cameri' # wherever 'Model Full Name' = Camery, change it to Cameri

df.loc[df['Model Full Name'] == 'Silverado', ['Model', 'Maker']] = ['SLR', 'GM'] # Multiple values get changed

df.loc[(df['Maker'] == 'Honda') & (df['Miles'] >= 50000), 'Covered?'] = 'Not Covered' # Multiple conditions



# 5) Add New Row
data = [{'Maker': 'Honda', 'Model': 'GLS'}]
df = df.append(data, ignore_index=True)



# 6) Delete Row
df.drop(df[df['Model'] == 'GLS'].index, inplace=True)
print(df)



# Save Changes
df.to_csv('modified.csv', index=False)