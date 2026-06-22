import pandas as pd

def find_value_difference(df, column_name):
    return df[column_name].max() - df[column_name].min()

if __name__ == '__main__':
    sample_data = {
        'numbers': [10, 20, 30, 40, 50]
    }
    df = pd.DataFrame(sample_data)
    print(find_value_difference(df, 'numbers'))