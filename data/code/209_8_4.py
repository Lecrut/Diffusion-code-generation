import pandas as pd

def calculate_mean(data):
    series = pd.Series(data)
    return series.mean()

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40]
    result = calculate_mean(sample_data)
    print(result)