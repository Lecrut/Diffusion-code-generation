import pandas as pd

def find_range(df, column_name):
    if column_name not in df.columns:
        return None
    min_val = df[column_name].min()
    max_val = df[column_name].max()
    return max_val - min_val

if __name__ == '__main__':
    sample_data = {
        'numbers': [3.14, 1.618, 2.718, 0.577, 9.999, -10.0, 5.0]
    }
    df = pd.DataFrame(sample_data)
    result = find_range(df, 'numbers')
    print(result)