import pandas as pd

def validate_series(series):
    if not isinstance(series, pd.Series) or series.empty:
        raise ValueError("Input must be a non-empty Pandas Series")

def calculate_mean(series):
    validate_series(series)
    return series.mean()

if __name__ == '__main__':
    sample_series = pd.Series([10, 20, 30, 40])
    mean_value = calculate_mean(sample_series)
    print(f"Mean of the series: {mean_value}")