import pandas as pd

def group_and_mean(df, group_cols, mean_cols):
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame.")
    
    if not all(isinstance(col, str) for col in group_cols + mean_cols):
        raise ValueError("Column names must be strings.")
    
    if not df[group_cols].isnull().values.any():
        raise ValueError("Group columns cannot contain null values.")
    
    grouped_df = df.groupby(group_cols)
    result = grouped_df[mean_cols].mean()
    return result

if __name__ == '__main__':
    data = {
        'id': [1, 2, 3, 4, 5],
        'category': ['A', 'B', 'A', 'C', 'B'],
        'value': [10, 20, 15, 25, 30]
    }
    
    df = pd.DataFrame(data)
    group_cols = ['category']
    mean_cols = ['value']
    
    result = group_and_mean(df, group_cols, mean_cols)
    print(result)