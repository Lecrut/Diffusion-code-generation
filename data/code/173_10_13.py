import pandas as pd

def calculate_mean_by_category():
    data = {'category': ['A', 'B', 'A', 'C', 'B', 'A'], 'value': [10, 20, 30, 40, 50, None]}
    df = pd.DataFrame(data)
    df['value'].fillna(df['value'].mean(), inplace=True)
    result = df.groupby('category')['value'].mean()
    return result
if __name__ == '__main__':
    print(calculate_mean_by_category())