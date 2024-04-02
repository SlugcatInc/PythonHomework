import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

one_hot = {'robot': [1, 0], 'human': [0, 1]}
encoded_data = pd.DataFrame(data['whoAmI'].apply(lambda x: one_hot[x]).tolist(), columns=['is_robot', 'is_human'])
final_data = pd.concat([data, encoded_data], axis=1)
final_data.head()