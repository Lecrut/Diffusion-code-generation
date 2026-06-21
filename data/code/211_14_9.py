import pandas as pd

def compute_mae(df1, df2):
    merged_df = pd.merge(df1, df2, on='common_id')
    mae = ((merged_df['column1'] - merged_df['column2']).abs()).mean()
    return mae

if __name__ == '__main__':
    sample_df1 = pd.DataFrame({
        'common_id': [1, 2, 3],
        'column1': [10, 20, 30]
    })
    
    sample_df2 = pd.DataFrame({
        'common_id': [1, 2, 3],
        'column2': [12, 18, 35]
    })
    
    result = compute_mae(sample_df1, sample_df2)
    print(result)