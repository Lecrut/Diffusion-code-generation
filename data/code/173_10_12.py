import pandas as pd

def calculate_category_means(data):
    df = pd.DataFrame(data)
    if not all((isinstance(x, (int, float)) for x in df['value'])):
        raise ValueError('All values must be numeric')
    df['value'] = df['value'].fillna(0)
    result = df.groupby('category')['value'].mean().reset_index()
    return result
if __name__ == '__main__':
    sample_data = {'category': ['A', 'B', 'A', 'C', 'B', 'A'], 'value': [10, 20, None, 30, 40, 50]}
    try:
        result = calculate_category_means(sample_data)
        print(result)
    except ValueError as e:
        print(e)