import pandas as pd

def process_weight_data(weight_data):
    df = pd.DataFrame(weight_data)
    df['Weight'] = pd.to_numeric(df['Weight'], errors='coerce')
    df = df.dropna(subset=['Weight'])
    df = df[df['Weight'] > 0]
    mean_weight = df['Weight'].mean()
    std_weight = df['Weight'].std()
    df['Standardized_Weight'] = (df['Weight'] - mean_weight) / std_weight
    return df

if __name__ == '__main__':
    sample_data = {
        'ID': [1, 2, 3, 4, 5],
        'Weight': ['70.5', '82.3', 'invalid', '91.0', '-5.0']
    }
    result = process_weight_data(sample_data)
    print(result)