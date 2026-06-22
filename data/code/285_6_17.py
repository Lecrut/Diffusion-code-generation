import pandas as pd

def compare_consecutive_elements(df, column_name):
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame")
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' not found in DataFrame")

    comparison_results = []
    for i in range(len(df[column_name]) - 1):
        if df[column_name][i] < df[column_name][i + 1]:
            comparison_results.append('increasing')
        elif df[column_name][i] > df[column_name][i + 1]:
            comparison_results.append('decreasing')
        else:
            comparison_results.append('equal')

    df['comparison'] = comparison_results
    return df

if __name__ == '__main__':
    sample_data = {
        'numbers': [1, 2, 3, 4, 5]
    }
    df = pd.DataFrame(sample_data)
    result_df = compare_consecutive_elements(df, 'numbers')
    print(result_df)