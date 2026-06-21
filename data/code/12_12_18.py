import numpy as np

def get_middle_element(arr):
    if not isinstance(arr, np.ndarray):
        raise TypeError("Input must be a numpy array")
    if arr.ndim != 1:
        raise ValueError("Input must be a 1-dimensional array")
    if len(arr) == 0:
        raise ValueError("Input array is empty")
    mid_index = len(arr) // 2
    return arr[mid_index]

if __name__ == '__main__':
    sample_arrays = [
        np.array([1, 2, 3, 4, 5]),
        np.array([10, 20, 30]),
        np.array([1, 2, 3, 4, 5, 6]),
        np.array([42]),
    ]
    for arr in sample_arrays:
        print(get_middle_element(arr))