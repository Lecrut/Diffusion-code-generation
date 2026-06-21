import pandas as pd

def compare_dataframes(df1, df2):
    common_columns = set(df1.columns).intersection(df2.columns)
    comparison_results = {}
    
    for column in common_columns:
        if df1[column].dtype == 'float64' and df2[column].dtype == 'float64':
            stats_df1 = df1[column].describe()
            stats_df2 = df2[column].describe()
            correlation = df1[column].corr(df2[column])
            comparison_results[column] = {
                'mean': (stats_df1['mean'], stats_df2['mean']),
                'median': (stats_df1['50%'], stats_df2['50%']),
                'std_dev': (stats_df1['std'], stats_df2['std']),
                'correlation': correlation
            }
    
    return comparison_results

if __name__ == '__main__':
    df1 = pd.DataFrame({
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1]
    })
    df2 = pd.DataFrame({
        'A': [2, 3, 4, 5, 6],
        'C': [7, 8, 9, 10, 11]
    })

    comparison_result = compare_dataframes(df1, df2)
    print(comparison_result)