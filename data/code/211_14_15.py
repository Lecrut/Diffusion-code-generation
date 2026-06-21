import pandas as pd

def load_and_merge_data():
    df1 = pd.DataFrame({
        'id': [1, 2, 3],
        'value1': [10, 20, 30]
    })
    
    df2 = pd.DataFrame({
        'id': [1, 2, 3],
        'value1': [12, 22, 32]
    })
    
    merged_df = pd.merge(df1, df2, on='id')
    return merged_df

def compute_mae(merged_df):
    mae = (abs(merged_df['value1_x'] - merged_df['value1_y']) / len(merged_df)).mean()
    return mae

if __name__ == '__main__':
    merged_data = load_and_merge_data()
    mae_result = compute_mae(merged_data)
    print(mae_result)