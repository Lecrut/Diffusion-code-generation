import pandas as pd
COLUMN_A = 'A'
COLUMN_B = 'B'
df1 = pd.DataFrame({COLUMN_A: [1, 2, 3, 4, 5], COLUMN_B: [5, 4, 3, 2, 1]})
df2 = pd.DataFrame({COLUMN_A: [2, 3, 4, 5, 6], COLUMN_B: [1, 2, 3, 4, 5]})

def compare_dataframes(df1, df2):
    comparison_results = {}
    for column in df1.columns:
        if column in df2.columns and df1[column].dtype == 'float64' and (df2[column].dtype == 'float64'):
            stats_df1 = df1[column].describe()
            stats_df2 = df2[column].describe()
            comparison_results[column] = {'mean': (stats_df1['mean'], stats_df2['mean']), 'median': (stats_df1['50%'], stats_df2['50%']), 'std_dev': (stats_df1['std'], stats_df2['std']), 'correlation': df1[column].corr(df2[column])}
    return comparison_results
if __name__ == '__main__':
    results = compare_dataframes(df1, df2)
    for column, stats in results.items():
        print(f'Column: {column}')
        print(f'  Mean: {stats['mean']}')
        print(f'  Median: {stats['median']}')
        print(f'  Standard Deviation: {stats['std_dev']}')
        print(f'  Correlation: {stats['correlation']}')