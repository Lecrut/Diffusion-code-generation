import pandas as pd
import io
import numpy as np

def process_weight_data(csv_content):
    df = pd.read_csv(io.StringIO(csv_content))
    df = df.dropna(subset=['weight_kg'])
    df['weight_kg'] = pd.to_numeric(df['weight_kg'], errors='coerce')
    df = df.dropna(subset=['weight_kg'])
    mean_weight = df['weight_kg'].mean()
    std_weight = df['weight_kg'].std()
    if std_weight == 0:
        df['standardized_weight'] = 0
    else:
        df['standardized_weight'] = (df['weight_kg'] - mean_weight) / std_weight
    return df

if __name__ == '__main__':
    sample_csv = "id,weight_kg,category\n1,70.5,A\n2,80.2,B\n3,,A\n4,65.0,C\n5,72.3,B\n"
    result_df = process_weight_data(sample_csv)
    print(result_df.to_string())