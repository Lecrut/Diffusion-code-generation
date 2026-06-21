import pandas as pd

def calculate_mean(series):
    return series.mean()

if __name__ == '__main__':
    sample_series = pd.Series([5, 15, 25, 35])
    mean_value = calculate_mean(sample_series)
    print(mean_value)