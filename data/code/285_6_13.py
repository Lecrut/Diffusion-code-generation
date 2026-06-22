import pandas as pd

def compare_consecutive_elements(df, column_name):
    return df[column_name].diff().apply(lambda x: 'increasing' if x > 0 else ('decreasing' if x < 0 else 'equal'))

if __name__ == '__main__':
    sample_data = {
        'values': [1, 2, 3, 4, 5]
    }
    df = pd.DataFrame(sample_data)
    result = compare_consecutive_elements(df, 'values')
    print(result)