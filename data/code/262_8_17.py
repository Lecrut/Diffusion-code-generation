import pandas as pd

def find_min_max(dataframe, column_name):
    min_value = dataframe[column_name].min()
    max_value = dataframe[column_name].max()
    return {'smallest': min_value, 'largest': max_value}

if __name__ == '__main__':
    sample_data = {
        'id': [1, 2, 3, 4, 5],
        'value': [10, 20, 5, 15, 25]
    }
    df = pd.DataFrame(sample_data)
    result = find_min_max(df, 'value')
    print(result)