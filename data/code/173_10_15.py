import pandas as pd

def validate_input(data):
    if not isinstance(data, dict) or 'category' not in data or 'value' not in data:
        raise ValueError("Input must be a dictionary with keys 'category' and 'value'")
    for value in data['value']:
        if not isinstance(value, (int, float)) and pd.isna(value):
            raise ValueError("Values in 'value' must be numbers or None")

def calculate_category_means(data):
    df = pd.DataFrame(data)
    validate_input(data)
    df['value'].fillna(0, inplace=True)
    result = df.groupby('category')['value'].mean().reset_index()
    return result

if __name__ == '__main__':
    sample_data = {
        'category': ['A', 'B', 'A', 'C', 'B', 'A'],
        'value': [10, 20, None, 30, 40, 50]
    }
    result = calculate_category_means(sample_data)
    print(result)