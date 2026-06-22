import numpy as np

def calculate_mean(data):
    if not isinstance(data, (list, tuple, np.ndarray)):
        raise TypeError("Input must be a list, tuple, or NumPy array.")
    data = np.asarray(data)
    if data.size == 0:
        raise ValueError("Input data cannot be empty.")
    if data.dtype.kind not in 'biufc':
        raise TypeError("Input data must contain numeric types.")
    return np.mean(data)

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    result = calculate_mean(sample_data)
    print(result)