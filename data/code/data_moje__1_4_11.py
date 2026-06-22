import pandas as pd
import io

def process_weight_data(file_content):
    df = pd.read_csv(io.StringIO(file_content))
    df.dropna(subset=['weight'], inplace=True)
    mean_weight = df['weight'].mean()
    std_weight = df['weight'].std()
    if std_weight == 0:
        df['standardized_weight'] = 0.0
    else:
        df['standardized_weight'] = (df['weight'] - mean_weight) / std_weight
    return df

if __name__ == '__main__':
    sample_csv = """id,name,weight
1,Alice,70.5
2,Bob,82.3
3,Charlie,65.0
4,Diana,78.2
5,Eve,70.5"""
    result_df = process_weight_data(sample_csv)
    print(result_df)