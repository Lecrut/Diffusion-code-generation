import pandas as pd

MEAN_SAMPLE_DATA = [10, 20, 30, 40]

def calculate_mean(data):
    series = pd.Series(data)
    return series.mean()

if __name__ == '__main__':
    mean_value = calculate_mean(MEAN_SAMPLE_DATA)
    print(f"Mean of the series: {mean_value}")