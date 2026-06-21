import pandas as pd

def compare_dataframes(df1, df2):
    result = {}
    for column in df1.columns:
        if column in df2.columns and pd.api.types.is_numeric_dtype(df1[column]) and pd.api.types.is_numeric_dtype(df2[column]):
            stats_df1 = df1[column].describe()
            stats_df2 = df2[column].describe()
            comparison = {
                'mean_diff': stats_df1['mean'] - stats_df2['mean'],
                'median_diff': stats_df1['50%'] - stats_df2['50%'],
                'std_dev_diff': stats_df1['std'] - stats_df2['std']
            }
            result[column] = comparison
    correlation_matrix = df1.corrwith(df2, axis=0)
    return result, correlation_matrix

if __name__ == '__main__':
    sample_df1 = pd.DataFrame({
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1],
        'C': ['a', 'b', 'c', 'd', 'e']
    })

    sample_df2 = pd.DataFrame({
        'A': [2, 3, 4, 5, 6],
        'B': [4, 3, 2, 1, 0],
        'D': ['f', 'g', 'h', 'i', 'j']
    })

    comparison_result, correlation_matrix = compare_dataframes(sample_df1, sample_df2)
    print("Comparison Result:", comparison_result)
    print("Correlation Matrix:\n", correlation_matrix)