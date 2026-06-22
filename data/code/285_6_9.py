import pandas as pd

def compare_consecutive_elements(df, column_name):
    df['Comparison'] = df[column_name].diff().apply(lambda x: 'increasing' if x > 0 else ('decreasing' if x < 0 else 'equal'))
    return df

if __name__ == '__main__':
    sample_data = {'Values': [10, 20, 15, 30, 25]}
    sample_df = pd.DataFrame(sample_data)
    result_df = compare_consecutive_elements(sample_df, 'Values')
    print(result_df)