import pandas as pd

def compare_consecutive_elements(df, column_name):
    df['comparison'] = df[column_name].diff().apply(lambda x: 'increasing' if x > 0 else ('decreasing' if x < 0 else 'equal'))
    return df

if __name__ == '__main__':
    sample_df = pd.DataFrame({'numbers': [1, 3, 2, 4, 5]})
    result_df = compare_consecutive_elements(sample_df, 'numbers')
    print(result_df)