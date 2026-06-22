import pandas as pd

def load_and_process_data(data):
    df = pd.DataFrame(data)
    df.dropna(inplace=True)
    df['Weight'] = pd.to_numeric(df['Weight'], errors='coerce')
    df.dropna(subset=['Weight'], inplace=True)
    mean_weight = df['Weight'].mean()
    std_weight = df['Weight'].std()
    df['Standardized_Weight'] = (df['Weight'] - mean_weight) / std_weight
    return df
if __name__ == '__main__':
    sample_data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Weight': [150, 200, None, 180]}
    processed_df = load_and_process_data(sample_data)
    print(processed_df)