import pandas as pd
from scipy.stats import zscore

def load_and_process_data(data):
    df = pd.DataFrame(data, columns=['weight'])
    df['weight'] = pd.to_numeric(df['weight'], errors='coerce')
    df.dropna(subset=['weight'], inplace=True)
    df['standardized_weight'] = zscore(df['weight'])
    return df
if __name__ == '__main__':
    sample_data = {'weight': [150, 200, 250, 'abc', 300, None, 350]}
    result_df = load_and_process_data(sample_data)
    print(result_df)