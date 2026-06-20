import numpy as np

def cumulative_sum(data):
    if not isinstance(data, np.ndarray) or data.ndim != 1:
        raise ValueError("Input must be a one-dimensional NumPy array.")
    
    return np.cumsum(data)

if __name__ == '__main__':
    sample_data = np.array([1, 2, 3, 4, 5])
    result = cumulative_sum(sample_data)
    print(result)