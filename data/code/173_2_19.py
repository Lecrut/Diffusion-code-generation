import pandas as pd

class DataFrameGrouper:
    def group_and_mean(self, df, group_cols, mean_cols):
        return df.groupby(group_cols)[mean_cols].mean().reset_index()

if __name__ == '__main__':
    data = {
        'id': [1, 2, 3, 4, 5],
        'category': ['A', 'B', 'A', 'C', 'B'],
        'value1': [10, 20, 15, 25, 30],
        'value2': [5, 10, 7, 12, 9]
    }
    df = pd.DataFrame(data)
    
    grouper = DataFrameGrouper()
    result = grouper.group_and_mean(df, ['category'], ['value1', 'value2'])
    print(result)