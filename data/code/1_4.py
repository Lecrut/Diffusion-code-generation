import pandas as pd
import io
import math

def process_weight_data(raw_csv_content):
    df = pd.read_csv(io.StringIO(raw_csv_content))
    
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
    sample_data = """id,name,weight
1,Alice,70
2,Bob,80
3,Charlie,75
4,David,NaN
5,Eve,0
6,Frank,85
7,Grace,90"""
    
    result_df = process_weight_data(sample_data)
    print(result_df[['name', 'weight', 'standardized_weight']].to_string(index=False))