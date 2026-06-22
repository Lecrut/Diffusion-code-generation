import pandas as pd
import numpy as np

def process_weight_data(raw_data):
    df = pd.read_csv(pd.io.common.StringIO(raw_data))
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].str.strip()
    df['weight'] = pd.to_numeric(df['weight'], errors='coerce')
    df = df.dropna(subset=['weight'])
    df = df[df['weight'] > 0]
    mean_weight = df['weight'].mean()
    std_weight = df['weight'].std()
    df['weight_standardized'] = (df['weight'] - mean_weight) / std_weight
    return df
if __name__ == '__main__':
    sample_data = 'name,weight\nAlice,70.5\nBob,85.2\nCharlie,60.1\nDiana,,\nEve,-5.0\nFrank,90.8\nGrace,abc\nHenry,75.3'
    result = process_weight_data(sample_data)
    print(result)