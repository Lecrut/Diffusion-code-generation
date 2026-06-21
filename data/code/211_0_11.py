import pandas as pd

def compare_dataframes(df1, df2):
    result = {}
    
    for column in df1.columns:
        if column in df2.columns and df1[column].dtype == 'float64' and df2[column].dtype == 'float64':
            result[column] = {
                'mean': {'df1': df1[column].mean(), 'df2': df2[column].mean()},
                'median': {'df1': df1[column].median(), 'df2': df2[column].median()},
                'std_dev': {'df1': df1[column].std(), 'df2': df2[column].std()},
                'correlation': {'df1_df2': df1[column].corr(df2[column])}
            }
    
    return result

if __name__ == '__main__':
    data1 = {
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1]
    }
    df1 = pd.DataFrame(data1)
    
    data2 = {
        'A': [2, 3, 4, 5, 6],
        'C': [10, 20, 30, 40, 50]
    }
    df2 = pd.DataFrame(data2)
    
    comparison_result = compare_dataframes(df1, df2)
    print(comparison_result)