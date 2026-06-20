import numpy as np

def calculate_cumulative_sum(data):
    return np.cumsum(data)

if __name__ == '__main__':
    sample_data = np.array([10, 20, 30, 40, 50])
    result = calculate_cumulative_sum(sample_data)
    print(result)