import pandas as pd

def find_extremes(df, column_name):
    if column_name not in df.columns:
        raise ValueError("Column not found in DataFrame")
    
    min_value = df[column_name].min()
    max_value = df[column_name].max()
    
    return {'smallest': min_value, 'largest': max_value}

if __name__ == '__main__':
    data = {
        'numbers': [15, 3, 8, 22, 1]
    }
    df = pd.DataFrame(data)
    result = find_extremes(df, 'numbers')
    print(result)