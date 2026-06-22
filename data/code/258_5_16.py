import pandas as pd

def calculate_average_pairs(df_column):
    if not isinstance(df_column, pd.Series) or len(df_column) % 2 != 0:
        raise ValueError("Input must be a pandas Series with an even number of elements")
    
    pairs = df_column.values.reshape(-1, 2)
    averages = (pairs[:, 0] + pairs[:, 1]) / 2
    return pd.Series(averages)

if __name__ == '__main__':
    sample_data = pd.Series([10, 5, 20, 8, 30, 12])
    result = calculate_average_pairs(sample_data)
    print(result)