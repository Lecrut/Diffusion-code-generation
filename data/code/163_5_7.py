import pandas as pd

def create_fruit_color_dataframe():
    fruit_color_dict = {
        "Apple": "Red",
        "Banana": "Yellow",
        "Cherry": "Red",
        "Date": "Brown",
        "Elderberry": "Purple"
    }
    df = pd.DataFrame(list(fruit_color_dict.items()), columns=["Fruit", "Color"])
    return df

if __name__ == '__main__':
    fruit_color_df = create_fruit_color_dataframe()
    print(fruit_color_df)