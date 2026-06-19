import pandas as pd

def load_and_process_data(data):
    df = pd.DataFrame(data)
    df.dropna(subset=['weight'], inplace=True)
    df['weight'] = pd.to_numeric(df['weight'], errors='coerce')
    df.dropna(subset=['weight'], inplace=True)
    mean_weight = df['weight'].mean()
    std_weight = df['weight'].std()
    df['standardized_weight'] = (df['weight'] - mean_weight) / std_weight
    return df
if __name__ == '__main__':
    sample_data = {'id': [1, 2, 3, 4, 5], 'weight': ['70', '80.5', 'abc', '90', None]}
    processed_df = load_and_process_data(sample_data)
    print(processed_df)