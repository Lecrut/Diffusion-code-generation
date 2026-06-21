import numpy as np

def validate_arrays(arr1, arr2):
    if not isinstance(arr1, np.ndarray) or not isinstance(arr2, np.ndarray):
        raise ValueError("Both inputs must be NumPy arrays.")
    if arr1.shape != arr2.shape:
        raise ValueError("Arrays must have the same shape.")

def compute_absolute_difference_and_sse(arr1, arr2):
    validate_arrays(arr1, arr2)
    abs_diff = np.abs(arr1 - arr2)
    sse = np.sum(abs_diff ** 2)
    return abs_diff, sse

if __name__ == '__main__':
    sample_arr1 = np.array([[1, 2], [3, 4]])
    sample_arr2 = np.array([[5, 6], [7, 8]])
    abs_diff, sse = compute_absolute_difference_and_sse(sample_arr1, sample_arr2)
    print("Absolute Difference Matrix:")
    print(abs_diff)
    print("Sum of Squared Errors:", sse)