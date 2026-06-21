import pandas as pd

def compute_series_mean(data):
    series = pd.Series(data)
    return series.mean()

if __name__ == '__main__':
    sample_data = [15, 25, 35, 45]
    mean_value = compute_series_mean(sample_data)
    print(f"Mean of the series: {mean_value}")