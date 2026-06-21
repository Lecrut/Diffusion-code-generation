import pandas as pd

def create_fruit_color_df():
    fruit_colors = {
        "Apple": "Red",
        "Banana": "Yellow",
        "Cherry": "Red",
        "Date": "Brown",
        "Elderberry": "Purple"
    }
    df = pd.DataFrame(list(fruit_colors.items()), columns=["Fruit", "Color"])
    return df

if __name__ == '__main__':
    fruit_color_df = create_fruit_color_df()
    print(fruit_color_df)