import pandas as pd

def find_range(df, column_name):
    if not isinstance(df, pd.DataFrame) or column_name not in df.columns:
        raise ValueError("Invalid input: df must be a pandas DataFrame and column_name must exist in the DataFrame")
    
    if df[column_name].empty:
        return None
    
    min_val = df[column_name].min()
    max_val = df[column_name].max()
    return max_val - min_val

if __name__ == '__main__':
    sample_df = pd.DataFrame({
        'numbers': [3.14, 1.618, 2.718, 0.577, 9.999, -10.0, 5.0]
    })
    result = find_range(sample_df, 'numbers')
    print(result)