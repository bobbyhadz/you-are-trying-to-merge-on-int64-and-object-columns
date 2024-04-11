import pandas as pd

df1 = pd.DataFrame({
    'year': [2020, 2021, 2022, 2023],
    'profit': [1500, 2500, 3500, 4500],
})

df2 = pd.DataFrame({
    'year': ['2020', '2021', '2022', '2023'],
    'employees': [10, 15, 20, 25],
})

print(df1['year'])

print(df2['year'])
