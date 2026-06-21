import pandas as pd

def calculate_grouped_means(data):
    df = pd.DataFrame(data)
    df['value'].fillna(0, inplace=True)
    grouped_means = df.groupby('category')['value'].mean().reset_index()
    return grouped_means

if __name__ == '__main__':
    sample_data = {
        'category': ['X', 'Y', 'X', 'Z', 'Y', 'X'],
        'value': [5, None, 10, 15, 20, 25]
    }
    result = calculate_grouped_means(sample_data)
    print(result)