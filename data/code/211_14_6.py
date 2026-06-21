import pandas as pd

class DataProcessor:
    def __init__(self):
        self.df1 = pd.DataFrame({'id': [1, 2, 3], 'value1': [10, 20, 30]})
        self.df2 = pd.DataFrame({'id': [1, 2, 3], 'value1': [12, 22, 32]})

    def load_and_merge_data(self):
        return pd.merge(self.df1, self.df2, on='id')

    def compute_mean_absolute_error(self, merged_df):
        return ((merged_df['value1_x'] - merged_df['value1_y']).abs()).mean()

if __name__ == '__main__':
    processor = DataProcessor()
    merged_data = processor.load_and_merge_data()
    mae_result = processor.compute_mean_absolute_error(merged_data)
    print(mae_result)