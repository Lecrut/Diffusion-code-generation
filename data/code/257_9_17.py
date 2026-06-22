import pandas as pd

def find_range(data):
    if not data.empty:
        return data.max() - data.min()
    else:
        return None

if __name__ == '__main__':
    sample_df = pd.DataFrame({'numbers': [3.14, 1.618, 2.718, 0.577, 9.999, -10.0, 5.0]})
    result = find_range(sample_df['numbers'])
    print(result)