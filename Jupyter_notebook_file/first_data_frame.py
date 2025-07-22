# First DataFrame
import pandas as pd

df3 = pd.DataFrame({'id': [1, 3, 4],'name': ['Alice', 'Bob', 'Charlie']})

df4 = pd.DataFrame({
    'id': [1, 2, 3],
    'age': [25,None, 35]
})

df4['age']=df4['age'].fillna('unknown')

result_merge = pd.merge(df3, df4, on='id', how='inner')

print(result_merge)