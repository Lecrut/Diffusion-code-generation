import pandas as pd

def calculate_category_means(data):
    df = pd.DataFrame(data)
    result = df.groupby('category')['value'].mean().reset_index()
    return result

if __name__ == '__main__':
    sample_data = {
        'category': ['A', 'B', 'A', 'C', 'B', 'A'],
        'value': [10, 20, 30, 40, 50, 60]
    }
    print(calculate_category_means(sample_data))