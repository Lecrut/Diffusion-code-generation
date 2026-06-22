import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_and_process_data(data):
    df = pd.DataFrame(data, columns=['Weight'])
    df['Weight'] = pd.to_numeric(df['Weight'], errors='coerce')
    df.dropna(subset=['Weight'], inplace=True)
    scaler = StandardScaler()
    df['Standardized_Weight'] = scaler.fit_transform(df[['Weight']])
    return df
if __name__ == '__main__':
    sample_data = [{'Weight': 70}, {'Weight': '80'}, {'Weight': None}, {'Weight': 60}, {'Weight': 'invalid'}]
    processed_df = load_and_process_data(sample_data)
    print(processed_df)