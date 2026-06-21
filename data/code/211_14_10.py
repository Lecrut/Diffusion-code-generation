import pandas as pd

def compute_mean_absolute_error(df1, df2):
    common_columns = df1.columns.intersection(df2.columns)
    return (df1[common_columns] - df2[common_columns]).abs().mean()

if __name__ == '__main__':
    sample_df1 = pd.DataFrame({
        'id': [1, 2, 3],
        'value1': [10, 20, 30],
        'value2': [15, 25, 35]
    })

    sample_df2 = pd.DataFrame({
        'id': [1, 2, 3],
        'value1': [12, 18, 32],
        'value2': [14, 26, 34]
    })

    result = compute_mean_absolute_error(sample_df1, sample_df2)
    print(result)