import pandas as pd

def calculate_mean_by_category(data):
    df = pd.DataFrame(data)
    result = df.groupby('category')['value'].mean().reset_index()
    return result

if __name__ == '__main__':
    sample_data = {
        'category': ['A', 'B', 'A', 'C', 'B', 'A'],
        'value': [10, 20, 30, 40, 50, 60]
    }
    result = calculate_mean_by_category(sample_data)
    print(result)