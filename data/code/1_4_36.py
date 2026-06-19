import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_and_process_data(data):
    df = pd.DataFrame(data, columns=['Weight'])
    df['Weight'].fillna(df['Weight'].mean(), inplace=True)
    scaler = StandardScaler()
    df['Standardized_Weight'] = scaler.fit_transform(df[['Weight']])
    return df
if __name__ == '__main__':
    sample_data = [[70], [80], [None], [60]]
    processed_df = load_and_process_data(sample_data)
    print(processed_df)