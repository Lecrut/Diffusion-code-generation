import pandas as pd
SAMPLE_DATA = [10, 20, 30, 40]

def calculate_mean(series):
    return series.mean()
if __name__ == '__main__':
    sample_series = pd.Series(SAMPLE_DATA)
    mean_value = calculate_mean(sample_series)
    print(f'Mean of the series: {mean_value}')