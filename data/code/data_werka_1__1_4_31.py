import pandas as pd

def load_and_process_weight_data(file_content):
    data = pd.read_csv(pd.compat.StringIO(file_content), sep='\t')
    data.dropna(subset=['Weight'], inplace=True)
    data['Weight'] = pd.to_numeric(data['Weight'], errors='coerce')
    data.dropna(subset=['Weight'], inplace=True)
    mean_weight = data['Weight'].mean()
    std_weight = data['Weight'].std()
    data['Standardized_Weight'] = (data['Weight'] - mean_weight) / std_weight
    return data
if __name__ == '__main__':
    sample_data = 'Name\tWeight\nAlice\t150\nBob\t\t200\nCharlie\t180\nDavid\tnot a number'
    processed_data = load_and_process_weight_data(sample_data)
    print(processed_data[['Name', 'Weight', 'Standardized_Weight']])