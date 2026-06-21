import pandas as pd

def compute_mean_absolute_error(df1, df2):
    common_columns = set(df1.columns) & set(df2.columns)
    if not common_columns:
        raise ValueError("No common columns to merge on")
    
    merged_df = pd.merge(df1, df2, on=list(common_columns), suffixes=('_left', '_right'))
    
    error_sum = 0
    for col in common_columns:
        if col.endswith('_left') or col.endswith('_right'):
            continue
        left_col = f"{col}_left"
        right_col = f"{col}_right"
        error_sum += (merged_df[left_col] - merged_df[right_col]).abs().sum()
    
    mean_error = error_sum / len(merged_df)
    return mean_error

if __name__ == '__main__':
    df1 = pd.DataFrame({
        'id': [1, 2, 3],
        'value1': [10, 20, 30],
        'value2': [15, 25, 35]
    })
    
    df2 = pd.DataFrame({
        'id': [1, 2, 3],
        'value1': [12, 22, 32],
        'value2': [14, 26, 34]
    })
    
    error = compute_mean_absolute_error(df1, df2)
    print(error)