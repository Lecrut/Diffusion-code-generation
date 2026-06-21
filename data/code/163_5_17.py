import pandas as pd

def dict_to_dataframe(fruit_color_dict):
    df = pd.DataFrame(list(fruit_color_dict.items()), columns=['Fruit', 'Color'])
    return df

if __name__ == '__main__':
    fruit_color_dict = {
        "Apple": "Red",
        "Banana": "Yellow",
        "Cherry": "Red",
        "Date": "Brown",
        "Elderberry": "Purple"
    }
    dataframe = dict_to_dataframe(fruit_color_dict)
    print(dataframe)