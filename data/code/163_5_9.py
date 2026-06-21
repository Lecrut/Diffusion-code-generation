import pandas as pd

def create_fruit_color_df(fruit_to_color):
    df = pd.DataFrame(list(fruit_to_color.items()), columns=['Fruit', 'Color'])
    return df

if __name__ == '__main__':
    fruit_to_color_dict = {
        "Apple": "Red",
        "Banana": "Yellow",
        "Cherry": "Red",
        "Date": "Brown",
        "Elderberry": "Purple"
    }
    df = create_fruit_color_df(fruit_to_color_dict)
    print(df)