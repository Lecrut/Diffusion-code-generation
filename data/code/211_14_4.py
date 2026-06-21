import pandas as pd

def load_and_merge_data():
    df1 = pd.DataFrame({'id': [1, 2, 3], 'value1': [10, 20, 30]})
    df2 = pd.DataFrame({'id': [1, 2, 3], 'value2': [12, 22, 32]})
    merged_df = pd.merge(df1, df2, on='id')
    return merged_df

def calculate_mean_absolute_error(merged_df):
    mae = (merged_df['value1'] - merged_df['value2']).abs().mean()
    return mae
if __name__ == '__main__':
    merged_data = load_and_merge_data()
    mae_result = calculate_mean_absolute_error(merged_data)
    print(mae_result)