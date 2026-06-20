import pandas as pd
import numpy as np
from io import StringIO

def process_weight_data(data):
    df = pd.read_csv(StringIO(data))
    df = df.dropna(subset=['weight'])
    df = df[df['weight'] > 0]
    mean_weight = df['weight'].mean()
    std_weight = df['weight'].std()
    if std_weight == 0:
        df['standardized_weight'] = 0.0
    else:
        df['standardized_weight'] = (df['weight'] - mean_weight) / std_weight
    return df

if __name__ == '__main__':
    sample_data = "name,weight\nAlice,70\nBob,80\nCharlie,65\nDiana,\nEve,75\nFrank,0\nGrace,90"
    result_df = process_weight_data(sample_data)
    print(result_df.to_string())