import pandas as pd

def find_min_max(df_column):
    if not isinstance(df_column, pd.Series) or df_column.empty:
        raise ValueError("Input must be a non-empty pandas Series")
    
    return {
        'smallest': df_column.min(),
        'largest': df_column.max()
    }

if __name__ == '__main__':
    sample_data = {'numbers': [15, 3, 8, 22, 1]}
    df = pd.DataFrame(sample_data)
    result = find_min_max(df['numbers'])
    print(result)