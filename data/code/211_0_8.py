import pandas as pd

def compare_dataframes(df1, df2):
    result = {}
    
    for col in df1.columns:
        if col in df2.columns:
            if df1[col].dtype == 'float64' or df1[col].dtype == 'int64':
                stats_df1 = df1[col].describe()
                stats_df2 = df2[col].describe()
                
                result[col] = {
                    'mean': (stats_df1['mean'], stats_df2['mean']),
                    'median': (stats_df1['50%'], stats_df2['50%']),
                    'std_dev': (stats_df1['std'], stats_df2['std']),
                    'correlation': df1[col].corr(df2[col])
                }
    
    return result

if __name__ == '__main__':
    df1 = pd.DataFrame({
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1]
    })
    
    df2 = pd.DataFrame({
        'A': [2, 3, 4, 5, 6],
        'C': [10, 20, 30, 40, 50]
    })
    
    comparison_result = compare_dataframes(df1, df2)
    print(comparison_result)