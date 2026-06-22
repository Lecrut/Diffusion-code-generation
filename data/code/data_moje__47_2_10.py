import numpy as np

def compute_mean(data):
    if not isinstance(data, (list, tuple, np.ndarray)):
        raise TypeError("Input data must be a list, tuple, or NumPy array")
    if len(data) == 0:
        raise ValueError("Input data must not be empty")
    data_array = np.asarray(data, dtype=float)
    if np.any(np.isnan(data_array)):
        raise ValueError("Input data must not contain NaN values")
    return float(np.mean(data_array))

if __name__ == '__main__':
    sample_data = [1.0, 2.0, 3.0, 4.0, 5.0]
    result = compute_mean(sample_data)
    print(result)