import pandas as pd
import numpy as np

def process_weight_data(input_file: str = None) -> pd.DataFrame:
    if input_file:
        df = pd.read_csv(input_file)
    else:
        df = pd.DataFrame({
            'weight': [55.5, 60.0, 120.0, 70.2, 85.3, 90.1, 45.0, 110.5, 65.8, 95.2]
        })
    
    df = df.dropna(subset=['weight'])
    df = df[df['weight'] > 0]
    
    mean_weight = df['weight'].mean()
    std_weight = df['weight'].std()
    
    df['standardized_weight'] = (df['weight'] - mean_weight) / std_weight
    
    return df

if __name__ == '__main__':
    result = process_weight_data()
    print(result.to_string(index=False))