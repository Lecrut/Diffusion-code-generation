import pandas as pd

def find_min_max(df, column_name):
    min_val = df[column_name].min()
    max_val = df[column_name].max()
    return {'smallest': min_val, 'largest': max_val}

if __name__ == '__main__':
    data = {
        'values': [15, 3, 8, 22, 1]
    }
    df = pd.DataFrame(data)
    result = find_min_max(df, 'values')
    print(result)