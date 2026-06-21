import pandas as pd

def create_fruit_color_df(fruits, colors):
    if not isinstance(fruits, dict) or not isinstance(colors, list):
        raise ValueError("Invalid input types. Expected fruits to be a dictionary and colors to be a list.")
    
    fruit_colors = []
    for fruit, color in fruits.items():
        if color in colors:
            fruit_colors.append((fruit, color))
    
    df = pd.DataFrame(fruit_colors, columns=['Fruit', 'Color'])
    return df

if __name__ == '__main__':
    fruits_dict = {"Apple": "Red", "Banana": "Yellow", "Cherry": "Red"}
    colors_list = ["Red", "Blue", "Green", "Yellow", "Purple"]
    df = create_fruit_color_df(fruits_dict, colors_list)
    print(df)