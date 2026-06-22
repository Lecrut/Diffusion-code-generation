import pandas as pd
import io

def process_weight_data(csv_content):
    df = pd.read_csv(io.StringIO(csv_content))
    df = df.dropna(subset=['weight'])
    df = df[df['weight'] > 0]
    mean_weight = df['weight'].mean()
    std_weight = df['weight'].std()
    if std_weight == 0:
        df['standardized_weight'] = 0.0
    else:
        df['standardized_weight'] = (df['weight'] - mean_weight) / std_weight
    return df

if __name__ == '__main__':
    sample_csv = "id,weight\n1,70\n2,75\n3,80\n4,\n5,65\n6,90"
    result_df = process_weight_data(sample_csv)
    print(result_df.to_string())