import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_and_clean_data(data):
    df = pd.DataFrame(data, columns=['weight'])
    df.drop_duplicates(inplace=True)
    df.dropna(subset=['weight'], inplace=True)
    return df

def standardize_weights(df):
    scaler = StandardScaler()
    df['standardized_weight'] = scaler.fit_transform(df[['weight']])
    return df
if __name__ == '__main__':
    sample_data = [{'weight': 68.5}, {'weight': 72.0}, {'weight': None}, {'weight': 68.5}, {'weight': 75.2}]
    cleaned_df = load_and_clean_data(sample_data)
    standardized_df = standardize_weights(cleaned_df)
    print(standardized_df)