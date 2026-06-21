import pandas as pd

class DataFrameComparator:
    def __init__(self, df1, df2):
        self.df1 = df1
        self.df2 = df2

    def compare(self):
        result = {}
        for column in self.df1.columns:
            if column in self.df2.columns and self.df1[column].dtype == 'float64' and self.df2[column].dtype == 'float64':
                stats_df1 = self.df1[column].describe()
                stats_df2 = self.df2[column].describe()
                result[column] = {
                    'mean': (stats_df1['mean'], stats_df2['mean']),
                    'median': (stats_df1['50%'], stats_df2['50%']),
                    'std_dev': (stats_df1['std'], stats_df2['std']),
                    'correlation': self.df1[column].corr(self.df2[column])
                }
        return result

if __name__ == '__main__':
    df1 = pd.DataFrame({
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1]
    })
    df2 = pd.DataFrame({
        'A': [1.5, 2.5, 3.5, 4.5, 5.5],
        'B': [4.5, 3.5, 2.5, 1.5, 0.5]
    })
    
    comparator = DataFrameComparator(df1, df2)
    comparison_result = comparator.compare()
    print(comparison_result)