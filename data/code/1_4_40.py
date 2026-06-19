import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_and_process_data(data):
    df = pd.DataFrame(data, columns=['weight'])
    df['weight'] = pd.to_numeric(df['weight'], errors='coerce')
    df.dropna(subset=['weight'], inplace=True)
    scaler = StandardScaler()
    df['standardized_weight'] = scaler.fit_transform(df[['weight']])
    return df
if __name__ == '__main__':
    sample_data = {'weight': [150, 200, 250, 'abc', 300, None, 350]}
    processed_df = load_and_process_data(sample_data)
    print(processed_df)