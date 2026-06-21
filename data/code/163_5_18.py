import pandas as pd

def create_fruit_color_df(fruit_color_dict):
    return pd.DataFrame(list(fruit_color_dict.items()), columns=['Fruit', 'Color'])

if __name__ == '__main__':
    fruit_color_dict = {
        "Apple": "Red",
        "Banana": "Yellow",
        "Cherry": "Red",
        "Date": "Brown",
        "Elderberry": "Purple"
    }
    df = create_fruit_color_df(fruit_color_dict)
    print(df)