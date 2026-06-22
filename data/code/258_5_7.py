import pandas as pd

def average_of_pairs(df):
    pairs = df[['pair_1', 'pair_2']].sum(axis=1)
    return pairs.mean()

if __name__ == '__main__':
    sample_df = pd.DataFrame({
        'pair_1': [10, 20, 30],
        'pair_2': [5, 8, 12]
    })
    result = average_of_pairs(sample_df)
    print(result)