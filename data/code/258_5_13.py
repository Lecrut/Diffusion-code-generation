import pandas as pd

def calculate_average_pairs(df, column_name):
    pairs = df[column_name].groupby(df.index // 2).mean()
    return pairs

if __name__ == '__main__':
    sample_data = {
        'A': [1, 2, 3, 4, 5, 6]
    }
    df = pd.DataFrame(sample_data)
    result = calculate_average_pairs(df, 'A')
    print(result)