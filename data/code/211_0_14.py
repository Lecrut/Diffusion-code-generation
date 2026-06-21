import pandas as pd

def compare_dataframes(df1, df2):
    result = {}
    for column in df1.columns:
        if column in df2.columns and pd.api.types.is_numeric_dtype(df1[column]) and pd.api.types.is_numeric_dtype(df2[column]):
            stats_df1 = df1[column].describe()
            stats_df2 = df2[column].describe()
            comparison = {
                'mean': (stats_df1['mean'], stats_df2['mean']),
                'median': (stats_df1['50%'], stats_df2['50%']),
                'std_dev': (stats_df1['std'], stats_df2['std']),
                'correlation': (df1[column].corr(df2[column]), None)
            }
            result[column] = comparison
    return result

if __name__ == '__main__':
    df1 = pd.DataFrame({
        'A': [1, 2, 3, 4],
        'B': [5, 6, 7, 8]
    })
    
    df2 = pd.DataFrame({
        'A': [2, 3, 4, 5],
        'C': [9, 10, 11, 12]
    })
    
    comparison_result = compare_dataframes(df1, df2)
    print(comparison_result)