import pandas as pd

def calculate_mean_by_category():
    data = {'category': ['A', 'B', 'A', 'C', 'B', 'A'], 'value': [10, 20, 30, 40, 50, 60]}
    df = pd.DataFrame(data)
    df['value'].fillna(0, inplace=True)
    result = df.groupby('category')['value'].mean().reset_index()
    return result
if __name__ == '__main__':
    result = calculate_mean_by_category()
    print(result)