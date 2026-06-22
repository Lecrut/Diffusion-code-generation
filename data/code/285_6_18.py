import pandas as pd

class ConsecutiveComparison:

    def compare_consecutives(self, df, column_name):
        if not isinstance(df, pd.DataFrame) or column_name not in df.columns:
            raise ValueError('Invalid DataFrame or column name')
        comparison_results = []
        for i in range(len(df) - 1):
            if df[column_name][i] < df[column_name][i + 1]:
                comparison_results.append('increasing')
            elif df[column_name][i] > df[column_name][i + 1]:
                comparison_results.append('decreasing')
            else:
                comparison_results.append('equal')
        comparison_results.append(None)
        return pd.Series(comparison_results, name='Comparison_Results')
if __name__ == '__main__':
    data = {'Numbers': [10, 20, 15, 30, 25, 40]}
    df = pd.DataFrame(data)
    comparer = ConsecutiveComparison()
    result = comparer.compare_consecutives(df, 'Numbers')
    print(result)