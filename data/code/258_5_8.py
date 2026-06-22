import pandas as pd

def calculate_average_pairs(df, column_name):
    if not isinstance(df, pd.DataFrame) or column_name not in df.columns:
        raise ValueError("Invalid input: DataFrame and column name must be provided.")
    
    paired_values = df[column_name].tolist()
    averages = [sum(pair) / 2 for pair in zip(paired_values[::2], paired_values[1::2])]
    return pd.Series(averages, name=f'{column_name}_average')

if __name__ == '__main__':
    sample_data = {'pairs': [(10, 5), (20, 8), (30, 12)]}
    df = pd.DataFrame(sample_data)
    result = calculate_average_pairs(df, 'pairs')
    print(result)