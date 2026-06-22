import pandas as pd

def calculate_average_pairs(df, column_name):
    return df[column_name].groupby(level=0).mean()

if __name__ == '__main__':
    data = {
        'A': [1, 2, 3, 4],
        'B': [5, 6, 7, 8]
    }
    index = pd.MultiIndex.from_tuples([('X', 1), ('X', 2), ('Y', 1), ('Y', 2)], names=['group', 'pair'])
    df = pd.DataFrame(data, index=index)
    result = calculate_average_pairs(df, 'A')
    print(result)