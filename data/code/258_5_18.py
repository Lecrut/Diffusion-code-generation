import pandas as pd

def calculate_average_pairs(df, column_name):
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame")
    
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' does not exist in the DataFrame")
    
    if len(df[column_name]) % 2 != 0:
        raise ValueError("DataFrame length for the specified column must be even to form pairs")
    
    averages = []
    for i in range(0, len(df[column_name]), 2):
        pair_average = (df[column_name].iloc[i] + df[column_name].iloc[i+1]) / 2
        averages.append(pair_average)
    
    return pd.Series(averages)

if __name__ == '__main__':
    sample_data = {'values': [10, 5, 20, 8, 30, 12]}
    df = pd.DataFrame(sample_data)
    result = calculate_average_pairs(df, 'values')
    print(result)