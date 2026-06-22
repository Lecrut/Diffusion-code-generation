import numpy as np

def compare_consecutive_elements(arr):
    if not isinstance(arr, np.ndarray) or arr.ndim != 1:
        raise ValueError("Input must be a one-dimensional numpy array")
    
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
    sample_array = np.array([1, 2, 3, 2, 1])
    result = compare_consecutive_elements(sample_array)
    print(result)