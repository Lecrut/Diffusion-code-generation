import pandas as pd

def group_and_mean(df, group_cols, mean_cols):
    return df.groupby(group_cols)[mean_cols].mean().reset_index()

if __name__ == '__main__':
    sample_data = {
        'id': [1, 2, 3, 4, 5],
        'category': ['A', 'B', 'A', 'C', 'B'],
        'value1': [10, 20, 15, 25, 30],
        'value2': [5, 10, 7, 12, 9]
    }
    sample_df = pd.DataFrame(sample_data)
    grouped_mean_df = group_and_mean(sample_df, ['category'], ['value1', 'value2'])
    print(grouped_mean_df)