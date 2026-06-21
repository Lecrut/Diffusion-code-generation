import pandas as pd

FRUITS = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
COLORS = ["Red", "Blue", "Green", "Yellow", "Purple"]

def create_fruit_color_df(fruits, colors):
    fruit_colors = [(fruit, color) for fruit in fruits for color in colors if fruit[0].lower() == color[0].lower()]
    return pd.DataFrame(fruit_colors, columns=["Fruit", "Color"])

if __name__ == '__main__':
    df = create_fruit_color_df(FRUITS, COLORS)
    print(df)