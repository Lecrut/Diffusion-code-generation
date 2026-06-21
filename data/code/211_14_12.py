import pandas as pd

def load_data():
    df1 = pd.DataFrame({'id': [1, 2, 3], 'value1': [10, 20, 30]})
    df2 = pd.DataFrame({'id': [1, 2, 3], 'value1': [12, 22, 32]})
    return df1, df2

def merge_dataframes(df1, df2):
    return pd.merge(df1, df2, on='id')

def compute_mae(merged_df):
    mae = ((merged_df['value1_x'] - merged_df['value1_y']).abs()).mean()
    return mae

if __name__ == '__main__':
    df1, df2 = load_data()
    merged_data = merge_dataframes(df1, df2)
    mae_result = compute_mae(merged_data)
    print(mae_result)