import pandas as pd
import numpy as np

def process_weight_data(raw_data: list) -> pd.DataFrame:
    df = pd.DataFrame(raw_data)
    if 'weight' not in df.columns:
        raise ValueError("DataFrame must contain a 'weight' column.")
    df['weight'] = pd.to_numeric(df['weight'], errors='coerce')
    df = df.dropna(subset=['weight'])
    df = df[df['weight'] > 0]
    mean_weight = df['weight'].mean()
    std_weight = df['weight'].std()
    if std_weight == 0:
        df['weight_standardized'] = 0
    else:
        df['weight_standardized'] = (df['weight'] - mean_weight) / std_weight
    return df
if __name__ == '__main__':
    sample_data = [{'id': 1, 'name': 'Alice', 'weight': 65.0}, {'id': 2, 'name': 'Bob', 'weight': 75.5}, {'id': 3, 'name': 'Charlie', 'weight': 'invalid'}, {'id': 4, 'name': 'Diana', 'weight': None}, {'id': 5, 'name': 'Eve', 'weight': -10.0}, {'id': 6, 'name': 'Frank', 'weight': 80.0}, {'id': 7, 'name': 'Grace', 'weight': 55.0}]
    result = process_weight_data(sample_data)
    print(result)