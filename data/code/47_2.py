import numpy as np

def calculate_mean(data):
    if not isinstance(data, (list, tuple, np.ndarray)):
        raise TypeError("Input must be a list, tuple, or numpy array")
    if len(data) == 0:
        raise ValueError("Input dataset cannot be empty")
    numeric_data = np.array(data, dtype=float)
    if np.any(np.isnan(numeric_data)):
        raise ValueError("Input dataset contains NaN values")
    mean_value = np.mean(numeric_data)
    return mean_value

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = calculate_mean(sample_data)
    print(result)