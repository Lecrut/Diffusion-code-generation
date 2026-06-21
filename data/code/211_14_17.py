import pandas as pd

def load_data():
    df1 = pd.DataFrame({
        'id': [4, 5, 6],
        'valueA': [100, 200, 300]
    })
    df2 = pd.DataFrame({
        'id': [4, 5, 6],
        'valueA': [105, 210, 315]
    })
    return df1, df2

def merge_dataframes(df1, df2):
    merged_df = pd.merge(df1, df2, on='id')
    return merged_df

def calculate_mae(merged_df):
    mae = ((merged_df['valueA_x'] - merged_df['valueA_y']).abs()).mean()
    return mae

if __name__ == '__main__':
    dataframes = load_data()
    merged_data = merge_dataframes(*dataframes)
    mae_result = calculate_mae(merged_data)
    print(mae_result)