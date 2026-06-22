import pandas as pd

def calculate_average_pairs(df, column_name):
    return df[column_name].rolling(window=2).mean().dropna()

if __name__ == '__main__':
    sample_data = {'A': [10, 20, 30, 40, 50]}
    df = pd.DataFrame(sample_data)
    result = calculate_average_pairs(df, 'A')
    print(result)