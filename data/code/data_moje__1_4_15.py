import pandas as pd
from io import StringIO

def process_weight_data():
    csv_data = """
weight_kg
65.5
70.2
abc
82.0
NaN
55.0
"""
    df = pd.read_csv(StringIO(csv_data))
    df['weight_kg'] = pd.to_numeric(df['weight_kg'], errors='coerce')
    df = df.dropna(subset=['weight_kg'])
    mean_w = df['weight_kg'].mean()
    std_w = df['weight_kg'].std()
    df['standardized_weight'] = (df['weight_kg'] - mean_w) / std_w
    return df[['weight_kg', 'standardized_weight']]

if __name__ == '__main__':
    result = process_weight_data()
    print(result)