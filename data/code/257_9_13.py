import pandas as pd

def find_value_difference(df, column_name):
    return df[column_name].max() - df[column_name].min()

if __name__ == '__main__':
    sample_df = pd.DataFrame({'values': [10, 20, 30, 40, 50]})
    print(find_value_difference(sample_df, 'values'))