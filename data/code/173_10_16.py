import pandas as pd

def calculate_mean_by_category():
    data = {'category': ['A', 'B', 'A', 'C', 'B', 'A'], 'value': [10, 20, None, 30, 40, 50]}
    df = pd.DataFrame(data)
    df['value'].fillna(df['value'].mean(), inplace=True)
    result = df.groupby('category')['value'].mean().reset_index()
    return result
if __name__ == '__main__':
    print(calculate_mean_by_category())