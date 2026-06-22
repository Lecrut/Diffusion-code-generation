import pandas as pd

def average_of_pairs(df, column_name):
    df[column_name] = (df[column_name].shift(-1) + df[column_name]) / 2
    return df[column_name].dropna()

if __name__ == '__main__':
    sample_data = {'values': [10, 20, 30, 40]}
    df = pd.DataFrame(sample_data)
    result = average_of_pairs(df, 'values')
    print(result)