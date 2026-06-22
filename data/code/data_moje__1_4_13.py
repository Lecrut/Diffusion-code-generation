import pandas as pd
import io

def process_weight_data(csv_content):
    df = pd.read_csv(io.StringIO(csv_content))
    df.dropna(subset=['weight'], inplace=True)
    df['weight'] = pd.to_numeric(df['weight'], errors='coerce')
    df.dropna(subset=['weight'], inplace=True)
    mean_weight = df['weight'].mean()
    std_weight = df['weight'].std()
    if std_weight == 0:
        df['standardized_weight'] = 0.0
    else:
        df['standardized_weight'] = (df['weight'] - mean_weight) / std_weight
    return df

if __name__ == '__main__':
    sample_data = "id,weight\n1,70\n2,75\n3,invalid\n4,80\n5,65"
    result_df = process_weight_data(sample_data)
    print(result_df['standardized_weight'].tolist())