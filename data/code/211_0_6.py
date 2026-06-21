import pandas as pd
df1 = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [5, 4, 3, 2, 1]})
df2 = pd.DataFrame({'A': [2, 3, 4, 5, 6], 'C': [10, 20, 30, 40, 50]})

def compare_dataframes(df1, df2):
    combined_df = pd.concat([df1, df2], axis=1)
    means = combined_df.mean()
    medians = combined_df.median()
    std_devs = combined_df.std()
    correlations = combined_df.corr()
    return (means, medians, std_devs, correlations)
if __name__ == '__main__':
    means, medians, std_devs, correlations = compare_dataframes(df1, df2)
    print('Means:\n', means)
    print('\nMedians:\n', medians)
    print('\nStandard Deviations:\n', std_devs)
    print('\nCorrelations:\n', correlations)