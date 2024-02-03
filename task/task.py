import pandas as pd

# Создание DataFrame
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Получение уникальных значений столбца
unique_values = data['whoAmI'].unique()

# Создание новых столбцов с префиксом 'is_'
for value in unique_values:
    data['is_' + value] = (data['whoAmI'] == value).astype(int)

data.head()
