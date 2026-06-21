import pandas as pd

def calculate_mean(data):
    return data.mean()

if __name__ == '__main__':
    sample_data = pd.Series([10, 20, 30, 40])
    result = calculate_mean(sample_data)
    print(result)