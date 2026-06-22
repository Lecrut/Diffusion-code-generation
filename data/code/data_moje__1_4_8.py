import pandas as pd
import io

def process_weight_data(raw_data_string):
    df = pd.read_csv(io.StringIO(raw_data_string))
    df = df.dropna(subset=['weight'])
    df['weight'] = pd.to_numeric(df['weight'], errors='coerce')
    df = df.dropna(subset=['weight'])
    mean_weight = df['weight'].mean()
    std_weight = df['weight'].std()
    if std_weight == 0:
        df['standardized_weight'] = 0.0
    else:
        df['standardized_weight'] = (df['weight'] - mean_weight) / std_weight
    return df
if __name__ == '__main__':
    sample_data = 'name,weight\nAlice,55.2\nBob,78.5\nCharlie,\nDave,abc\nEve,62.1\nFrank,59.8\nGrace,71.3\n'
    result_df = process_weight_data(sample_data)
    print(result_df)