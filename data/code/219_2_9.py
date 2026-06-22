import numpy as np

def find_max_in_array(arr):
    if not isinstance(arr, np.ndarray) or arr.ndim != 1:
        raise ValueError("Input must be a one-dimensional NumPy array")
    return np.max(arr)

if __name__ == '__main__':
    sample_data = np.array([10, 5, 20, 8, 15])
    max_value = find_max_in_array(sample_data)
    print(f"Maximum of {sample_data}: {max_value}")