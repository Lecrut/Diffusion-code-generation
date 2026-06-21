import pandas as pd

def create_fruit_color_df(fruits, colors):
    if not isinstance(fruits, dict) or not isinstance(colors, list):
        raise ValueError("Invalid input types. 'fruits' must be a dictionary and 'colors' must be a list.")
    
    df = pd.DataFrame(list(fruits.items()), columns=['Fruit', 'Primary Color'])
    return df

if __name__ == '__main__':
    fruit_color_map = {
        "Apple": "Red",
        "Banana": "Yellow",
        "Cherry": "Red",
        "Date": "Brown",
        "Elderberry": "Purple"
    }
    
    colors_list = ["Red", "Blue", "Green", "Yellow", "Purple"]
    
    try:
        df = create_fruit_color_df(fruit_color_map, colors_list)
        print(df)
    except ValueError as e:
        print(e)