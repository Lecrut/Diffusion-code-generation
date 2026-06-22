import pandas as pd

def compare_consecutive_elements(df, column_name):
    df['Comparison'] = df[column_name].diff().apply(lambda x: 'increasing' if x > 0 else ('decreasing' if x < 0 else 'equal'))
    return df

if __name__ == '__main__':
    sample_df = pd.DataFrame({'Values': [1, 2, 3, 2, 4]})
    result_df = compare_consecutive_elements(sample_df, 'Values')
    print(result_df)