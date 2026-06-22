import pandas as pd

def find_min_max(df, column_name):
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame")
    
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' does not exist in the DataFrame")
    
    min_value = df[column_name].min()
    max_value = df[column_name].max()
    
    return {'smallest': min_value, 'largest': max_value}

if __name__ == '__main__':
    data = {
        'numbers': [15, 3, 8, 22, 1]
    }
    df = pd.DataFrame(data)
    result = find_min_max(df, 'numbers')
    print(result)