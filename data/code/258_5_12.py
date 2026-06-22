import pandas as pd

def calculate_average_pairs(df, column_name):
    pairs = df[column_name].tolist()
    averages = [(pairs[i] + pairs[i+1]) / 2 for i in range(0, len(pairs), 2)]
    return pd.Series(averages)

if __name__ == '__main__':
    sample_data = {'values': [10, 5, 20, 8, 30, 12]}
    df = pd.DataFrame(sample_data)
    result_series = calculate_average_pairs(df, 'values')
    print(result_series)