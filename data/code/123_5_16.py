import numpy as np

def validate_input(data):
    if not isinstance(data, np.ndarray) or data.ndim != 1:
        raise ValueError("Input must be a one-dimensional NumPy array")

def cumulative_sum(data):
    validate_input(data)
    return np.cumsum(data)

if __name__ == '__main__':
    sample_data = np.array([10, 20, 30, 40, 50])
    result = cumulative_sum(sample_data)
    print(result)