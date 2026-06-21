import pandas as pd

def validate_dataframe(df):
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame")
    if df.empty:
        raise ValueError("DataFrame cannot be empty")

def calculate_group_means(df, group_cols, mean_cols):
    validate_dataframe(df)
    return df.groupby(group_cols)[mean_cols].mean()

if __name__ == '__main__':
    sample_data = {
        'id': [1, 2, 3, 4, 5],
        'category': ['A', 'B', 'A', 'C', 'B'],
        'value1': [10, 20, 15, 25, 30],
        'value2': [1, 2, 3, 4, 5]
    }
    sample_df = pd.DataFrame(sample_data)
    grouped_means = calculate_group_means(sample_df, ['category'], ['value1', 'value2'])
    print(grouped_means)