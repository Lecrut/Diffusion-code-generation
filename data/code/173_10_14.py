import pandas as pd

def calculate_mean_by_category():
    data = {'category': ['A', 'B', 'A', 'C', 'B', 'A'], 'value': [10, 20, 30, 40, 50, None]}
    df = pd.DataFrame(data)
    mean_value = df['value'].mean()
    df['value'] = df['value'].fillna(mean_value)
    result = df.groupby('category')['value'].mean().reset_index()
    return result
if __name__ == '__main__':
    result = calculate_mean_by_category()
    print(result)