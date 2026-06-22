import pandas as pd

def find_min_max(df, column_name):
    return {'smallest': df[column_name].min(), 'largest': df[column_name].max()}

if __name__ == '__main__':
    data = {
        'numbers': [15, 3, 8, 22, 1]
    }
    df = pd.DataFrame(data)
    result = find_min_max(df, 'numbers')
    print(result)