import numpy as np

def validate_arrays(arr1, arr2):
    if not (isinstance(arr1, np.ndarray) and isinstance(arr2, np.ndarray)):
        raise ValueError("Both arguments must be NumPy arrays.")
    if arr1.shape != arr2.shape:
        raise ValueError("Arrays must have the same shape.")

def calculate_difference(arr1, arr2):
    validate_arrays(arr1, arr2)
    return arr2 - arr1

if __name__ == '__main__':
    sample_arr1 = np.array([i for i in range(10000)])
    sample_arr2 = np.array([i * 3 for i in range(10000)])
    result = calculate_difference(sample_arr1, sample_arr2)
    print(result)