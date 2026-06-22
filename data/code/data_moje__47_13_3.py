import numpy as np

def calculate_mean(data_points):
    if not isinstance(data_points, (list, tuple, np.ndarray)):
        raise TypeError("Input must be a list, tuple, or numpy array")
    if len(data_points) == 0:
        raise ValueError("Input data must not be empty")
    data_array = np.asarray(data_points, dtype=float)
    if not np.all(np.isfinite(data_array)):
        raise ValueError("Input data must contain only finite numbers")
    return np.mean(data_array)

if __name__ == '__main__':
    fixed_sequence = [23.4, 45.6, 12.3, 67.8, 34.5, 89.1, 2.7]
    computed_mean = calculate_mean(fixed_sequence)
    print(computed_mean)