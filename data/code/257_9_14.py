import pandas as pd

def find_range(data):
    return data.max() - data.min()

if __name__ == '__main__':
    sample_data = {'numeric_values': [3.14, 1.618, 2.718, 0.577, 9.999, -10.0, 5.0]}
    df = pd.DataFrame(sample_data)
    result = find_range(df['numeric_values'])
    print(result)