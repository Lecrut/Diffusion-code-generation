import pandas as pd
from scipy.stats import zscore

def load_and_process_data(data):
    df = pd.DataFrame(data, columns=['Weight'])
    df['Weight'] = pd.to_numeric(df['Weight'], errors='coerce')
    df.dropna(subset=['Weight'], inplace=True)
    df['Standardized_Weight'] = zscore(df['Weight'])
    return df
if __name__ == '__main__':
    sample_data = [{'Weight': 70}, {'Weight': '80'}, {'Weight': 'invalid'}, {'Weight': 90.5}]
    result_df = load_and_process_data(sample_data)
    print(result_df)