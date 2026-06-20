import numpy as np

def validate_data(data):
    if not isinstance(data, np.ndarray) or data.ndim != 1:
        raise ValueError('Input must be a one-dimensional NumPy array.')

def cumulative_sum(data):
    validate_data(data)
    return np.cumsum(data)
if __name__ == '__main__':
    sample_data = np.array([1, 2, 3, 4, 5])
    result = cumulative_sum(sample_data)
    print(result)