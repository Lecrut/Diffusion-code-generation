import numpy as np

def compute_cumulative_sum(data):
    return np.cumsum(data)

if __name__ == '__main__':
    sample_data = np.array([1, 2, 3, 4, 5])
    result = compute_cumulative_sum(sample_data)
    print(result)