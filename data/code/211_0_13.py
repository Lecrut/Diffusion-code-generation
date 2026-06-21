import pandas as pd
df1 = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [5, 4, 3, 2, 1]})
df2 = pd.DataFrame({'A': [2, 3, 4, 5, 6], 'B': [2, 3, 4, 5, 6]})

def compare_dataframes(df1, df2):
    stats_df1 = df1.describe()
    stats_df2 = df2.describe()
    print('Statistics for DataFrame 1:')
    print(stats_df1)
    print('\nStatistics for DataFrame 2:')
    print(stats_df2)
if __name__ == '__main__':
    compare_dataframes(df1, df2)