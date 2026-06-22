import pandas as pd
import numpy as np

def process_weight_data(data: pd.DataFrame) -> pd.DataFrame:
    cleaned_data = data.dropna(subset=['weight'])
    cleaned_data['weight'] = pd.to_numeric(cleaned_data['weight'], errors='coerce')
    valid_data = cleaned_data.dropna(subset=['weight'])
    mean_weight = valid_data['weight'].mean()
    std_weight = valid_data['weight'].std()
    if std_weight == 0 or pd.isna(std_weight):
        valid_data['standardized_weight'] = 0.0
    else:
        valid_data['standardized_weight'] = (valid_data['weight'] - mean_weight) / std_weight
    result = pd.DataFrame()
    result['id'] = valid_data['id']
    result['weight'] = valid_data['weight']
    result['standardized_weight'] = valid_data['standardized_weight']
    return result

if __name__ == '__main__':
    sample_data = pd.DataFrame({
        'id': [1, 2, 3, 4, 5],
        'weight': [70.5, 65.0, 72.0, np.nan, 68.0]
    })
    result = process_weight_data(sample_data)
    print(result)