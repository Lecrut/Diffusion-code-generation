import pandas as pd
from io import StringIO

def process_weight_data(csv_data: str) -> pd.DataFrame:
    df = pd.read_csv(StringIO(csv_data))
    numeric_cols = ['weight_kg']
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    df = df.dropna(subset=['weight_kg'])
    mean_weight = df['weight_kg'].mean()
    std_weight = df['weight_kg'].std()
    if std_weight == 0:
        df['standardized_weight'] = 0.0
    else:
        df['standardized_weight'] = (df['weight_kg'] - mean_weight) / std_weight
    return df

if __name__ == '__main__':
    sample_data = """id,weight_kg
1,50.0
2,60.0
3,70.0
4,80.0
5,90.0"""
    result = process_weight_data(sample_data)
    print(result[['id', 'weight_kg', 'standardized_weight']])