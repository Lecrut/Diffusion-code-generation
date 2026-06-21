import pandas as pd

def load_and_merge_dataframes():
    df1 = pd.DataFrame({
        'id': [1, 2, 3],
        'value1': [10, 20, 30]
    })
    
    df2 = pd.DataFrame({
        'id': [1, 2, 3],
        'value1': [12, 18, 35]
    })
    
    merged_df = pd.merge(df1, df2, on='id')
    return merged_df

def compute_mean_absolute_error(merged_df):
    error = abs(merged_df['value1_x'] - merged_df['value1_y'])
    mean_error = error.mean()
    return mean_error

if __name__ == '__main__':
    merged_data = load_and_merge_dataframes()
    mae = compute_mean_absolute_error(merged_data)
    print(mae)