import pandas as pd

class DataFrameGrouper:
    def __init__(self, data):
        self.df = pd.DataFrame(data)

    def group_and_mean(self, group_cols, mean_cols):
        grouped_df = self.df.groupby(group_cols)[mean_cols].mean().reset_index()
        return grouped_df

if __name__ == '__main__':
    sample_data = {
        'id': [1, 2, 3, 4, 5],
        'category': ['A', 'B', 'A', 'C', 'B'],
        'value1': [10, 20, 15, 25, 30],
        'value2': [5, 10, 7, 12, 9]
    }
    
    grouper = DataFrameGrouper(sample_data)
    result = grouper.group_and_mean(['category'], ['value1', 'value2'])
    print(result)