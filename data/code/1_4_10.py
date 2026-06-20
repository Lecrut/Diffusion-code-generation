import pandas as pd
import io

def process_weight_data(file_content: str) -> pd.DataFrame:
    df = pd.read_csv(io.StringIO(file_content))
    
    df.dropna(subset=['weight'], inplace=True)
    df['weight'] = pd.to_numeric(df['weight'], errors='coerce')
    df = df.dropna(subset=['weight'])
    
    weight_mean = df['weight'].mean()
    weight_std = df['weight'].std()
    
    if weight_std == 0:
        df['standardized_weight'] = 0
    else:
        df['standardized_weight'] = (df['weight'] - weight_mean) / weight_std
    
    return df

if __name__ == '__main__':
    sample_csv = "name,weight,age\nAlice,70,25\nBob,80,30\nCharlie,65,28\nDave,85,35\nEve,75,22"
    result_df = process_weight_data(sample_csv)
    print(result_df.to_string(index=False))