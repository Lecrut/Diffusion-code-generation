import pandas as pd

def calculate_mean(series):
    if not isinstance(series, pd.Series):
        raise ValueError("Input must be a pandas Series")
    return series.mean()

if __name__ == '__main__':
    sample_series = pd.Series([10, 20, 30, 40])
    mean_value = calculate_mean(sample_series)
    print(f"Mean of the series: {mean_value}")