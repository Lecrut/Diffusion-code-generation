import numpy as np

def validate_input(data):
    if not isinstance(data, np.ndarray) or data.ndim != 1:
        raise ValueError("Input must be a one-dimensional NumPy array.")

def cumulative_sum_vectorized(data):
    validate_input(data)
    return np.cumsum(data)

if __name__ == '__main__':
    sample_data = np.array([1, 2, 3, 4, 5])
    result = cumulative_sum_vectorized(sample_data)
    print(result)