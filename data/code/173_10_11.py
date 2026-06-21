import pandas as pd

def calculate_mean_by_category():
    data = {
        'category': ['A', 'B', 'A', 'C', 'B', 'A'],
        'value': [10, 20, 30, 40, 50, None]
    }
    df = pd.DataFrame(data)
    result = df.groupby('category')['value'].mean(skipna=True).reset_index()
    return result

if __name__ == '__main__':
    print(calculate_mean_by_category())