import pandas as pd

def max_value(series):
    return series.max()

if __name__ == '__main__':
    sample_series = pd.Series([3, 5, 1, 2, 4])
    print(max_value(sample_series))