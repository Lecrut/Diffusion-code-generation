import numpy as np

def validate_array(arr):
    if not isinstance(arr, np.ndarray):
        raise ValueError("Input must be a numpy array.")
    if arr.ndim != 1:
        raise ValueError("Input must be a one-dimensional numpy array.")

def compare_consecutive_elements(arr):
    results = []
    for i in range(len(arr) - 1):
        if arr[i] < arr[i + 1]:
            results.append('increasing')
        elif arr[i] > arr[i + 1]:
            results.append('decreasing')
        else:
            results.append('equal')
    return results

if __name__ == '__main__':
    sample_array = np.array([1, 2, 5, 4, 3, 8, 9, 10])
    validate_array(sample_array)
    result = compare_consecutive_elements(sample_array)
    print(result)