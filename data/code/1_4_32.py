import pandas as pd

def load_and_process_weight_data(file_content):
    df = pd.read_csv(pd.compat.StringIO(file_content), sep='\t')
    df.dropna(subset=['Weight'], inplace=True)
    df['Weight'] = pd.to_numeric(df['Weight'], errors='coerce')
    df.dropna(subset=['Weight'], inplace=True)
    mean_weight = df['Weight'].mean()
    std_weight = df['Weight'].std()
    df['Standardized_Weight'] = (df['Weight'] - mean_weight) / std_weight
    return df
if __name__ == '__main__':
    sample_data = 'Name\tWeight\nAlice\t70\nBob\t\t65\nCharlie\t80\nDavid\tnot a number\nEve\t75'
    result_df = load_and_process_weight_data(sample_data)
    print(result_df)