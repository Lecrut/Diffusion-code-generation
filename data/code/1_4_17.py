import pandas as pd
import numpy as np

def load_and_standardize_weight_data(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    required_columns = ['ID', 'Weight_KG']
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f'Missing column: {col}')
    df = df.dropna(subset=['Weight_KG'])
    df['Weight_KG'] = pd.to_numeric(df['Weight_KG'], errors='coerce')
    df = df.dropna(subset=['Weight_KG'])
    mean_weight = df['Weight_KG'].mean()
    std_weight = df['Weight_KG'].std()
    if std_weight == 0:
        df['Weight_Standardized'] = 0.0
    else:
        df['Weight_Standardized'] = (df['Weight_KG'] - mean_weight) / std_weight
    return df

def generate_sample_data():
    data = {'ID': [1, 2, 3, 4, 5], 'Weight_KG': [70.5, 65.0, 80.2, 72.1, 68.4]}
    return pd.DataFrame(data)
if __name__ == '__main__':
    sample_df = generate_sample_data()
    result_df = load_and_standardize_weight_data('/dev/null')
    import tempfile
    import os
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        sample_df.to_csv(f, index=False)
        temp_file_path = f.name
    try:
        result_df = load_and_standardize_weight_data(temp_file_path)
        print(result_df[['ID', 'Weight_KG', 'Weight_Standardized']])
    finally:
        os.unlink(temp_file_path)