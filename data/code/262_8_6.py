import pandas as pd

def find_min_max(df, column_name):
    if not isinstance(df, pd.DataFrame) or column_name not in df.columns:
        raise ValueError("Invalid input: Ensure the first argument is a pandas DataFrame and the second argument is a valid column name.")
    
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