import pandas as pd
import numpy as np

def process_weight_data(weights_raw: list) -> pd.DataFrame:
    df = pd.DataFrame(weights_raw, columns=['weight_kg'])
    df['weight_kg'] = pd.to_numeric(df['weight_kg'], errors='coerce')
    df = df.dropna(subset=['weight_kg'])
    mean_weight = df['weight_kg'].mean()
    std_weight = df['weight_kg'].std()
    if std_weight == 0:
        df['standardized_weight'] = 0.0
    else:
        df['standardized_weight'] = (df['weight_kg'] - mean_weight) / std_weight
    return df

if __name__ == '__main__':
    sample_weights = [150, 155, 160, 165, 170, 175, 180, 'invalid', None, 190]
    result_df = process_weight_data(sample_weights)
    print(result_df)