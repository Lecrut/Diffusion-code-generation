import pandas as pd

def calculate_range(dataframe, column_name):
    min_val = dataframe[column_name].min()
    max_val = dataframe[column_name].max()
    return max_val - min_val

if __name__ == '__main__':
    sample_data = {
        'numbers': [3.14, 1.618, 2.718, 0.577, 9.999, -10.0, 5.0]
    }
    df = pd.DataFrame(sample_data)
    result = calculate_range(df, 'numbers')
    print(result)