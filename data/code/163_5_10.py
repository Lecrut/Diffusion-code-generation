import pandas as pd

def dict_to_dataframe(fruit_color_dict):
    return pd.DataFrame(list(fruit_color_dict.items()), columns=['Fruit', 'Color'])

if __name__ == '__main__':
    fruit_colors = {
        'apple': 'red',
        'banana': 'yellow',
        'grape': 'purple'
    }
    df = dict_to_dataframe(fruit_colors)
    print(df)