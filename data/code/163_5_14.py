import pandas as pd

def dict_to_dataframe(fruit_color_dict):
    return pd.DataFrame(list(fruit_color_dict.items()), columns=['Fruit', 'Color'])

if __name__ == '__main__':
    sample_data = {'Apple': 'Red', 'Banana': 'Yellow', 'Cherry': 'Red'}
    df = dict_to_dataframe(sample_data)
    print(df)