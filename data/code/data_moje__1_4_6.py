import pandas as pd
import numpy as np

def process_weight_data(filename):
    df = pd.read_csv(filename)
    df['Weight'] = pd.to_numeric(df['Weight'], errors='coerce')
    df = df.dropna(subset=['Weight'])
    df = df[df['Weight'] > 0]
    mean_weight = df['Weight'].mean()
    std_weight = df['Weight'].std()
    df['StandardizedWeight'] = (df['Weight'] - mean_weight) / std_weight
    return df

if __name__ == '__main__':
    sample_data = "Name,Weight\nAlice,70\nBob,80\nCharlie,60\nDavid,90\nEve,75\n"
    import io
    pd.io.common.StringIO(sample_data)
    sample_df = pd.read_csv(io.StringIO(sample_data))
    processed_df = process_weight_data(io.StringIO(sample_data))
    print(processed_df)