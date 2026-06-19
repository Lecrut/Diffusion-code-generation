import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_and_process_weight_data(data):
    df = pd.DataFrame(data, columns=['weight'])
    df['weight'].fillna(df['weight'].mean(), inplace=True)
    scaler = StandardScaler()
    df['standardized_weight'] = scaler.fit_transform(df[['weight']])
    return df
if __name__ == '__main__':
    sample_data = [{'weight': 70}, {'weight': None}, {'weight': 80}, {'weight': 60}]
    processed_df = load_and_process_weight_data(sample_data)
    print(processed_df)