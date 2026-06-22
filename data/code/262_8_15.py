import pandas as pd

def find_min_max(df, column_name):
    return df[column_name].min(), df[column_name].max()

if __name__ == '__main__':
    sample_data = {'numbers': [10, 20, 30, 40, 50]}
    sample_df = pd.DataFrame(sample_data)
    min_val, max_val = find_min_max(sample_df, 'numbers')
    print(f"Minimum: {min_val}, Maximum: {max_val}")