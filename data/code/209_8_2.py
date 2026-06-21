import pandas as pd

def calculate_mean(series):
    return series.mean()

if __name__ == '__main__':
    sample_series = pd.Series([10, 20, 30, 40])
    print(calculate_mean(sample_series))