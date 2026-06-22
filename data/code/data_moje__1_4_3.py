import pandas as pd
import io

def process_weight_data(csv_content):
    df = pd.read_csv(io.StringIO(csv_content))
    df['weight'] = pd.to_numeric(df['weight'], errors='coerce')
    df = df.dropna(subset=['weight'])
    mean_weight = df['weight'].mean()
    std_weight = df['weight'].std()
    df['std_weight'] = (df['weight'] - mean_weight) / std_weight
    return df

if __name__ == '__main__':
    sample_data = """id,weight,unit
1,70.5,kg
2,82.0,kg
3,65.0,kg
4,90.5,kg
5,75.0,kg"""
    result_df = process_weight_data(sample_data)
    print(result_df[['id', 'weight', 'std_weight']].to_string(index=False))