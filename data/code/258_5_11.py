import pandas as pd

def calculate_average_pairs(df, column_name):
    if not isinstance(df, pd.DataFrame) or column_name not in df.columns:
        raise ValueError("Invalid DataFrame or column name")
    
    pairs = df[column_name].apply(lambda x: (x[0], x[1]))
    averages = pairs.apply(lambda pair: sum(pair) / len(pair))
    return averages

if __name__ == '__main__':
    sample_data = {'pairs': [(10, 5), (20, 8), (30, 12)]}
    df = pd.DataFrame(sample_data)
    result = calculate_average_pairs(df, 'pairs')
    print(result)