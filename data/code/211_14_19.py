import pandas as pd

def load_and_merge_data():
    df1 = pd.DataFrame({
        'id': [1, 2, 3],
        'value1': [10, 20, 30]
    })
    
    df2 = pd.DataFrame({
        'id': [1, 2, 4],
        'value2': [15, 25, 35]
    })
    
    merged_df = pd.merge(df1, df2, on='id', how='inner')
    return merged_df

def compute_mean_absolute_error(merged_df):
    mae = ((merged_df['value1'] - merged_df['value2']).abs()).mean()
    return mae

if __name__ == '__main__':
    merged_data = load_and_merge_data()
    mae_result = compute_mean_absolute_error(merged_data)
    print(mae_result)