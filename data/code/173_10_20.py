import pandas as pd

def validate_data(df):
    if 'category' not in df.columns or 'value' not in df.columns:
        raise ValueError("DataFrame must contain 'category' and 'value' columns")

def group_and_calculate_means(df):
    validate_data(df)
    df['value'] = df['value'].fillna(0)
    result = df.groupby('category')['value'].mean().reset_index()
    return result
if __name__ == '__main__':
    sample_data = {'category': ['A', 'B', 'A', 'C', 'B', 'A'], 'value': [10, 20, None, 30, 40, 50]}
    df = pd.DataFrame(sample_data)
    result = group_and_calculate_means(df)
    print(result)