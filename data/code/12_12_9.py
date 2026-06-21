import numpy as np

def get_middle_element(arr):
    if not isinstance(arr, np.ndarray):
        raise TypeError("Input must be a numpy array")
    if arr.ndim != 1:
        raise ValueError("Input must be a 1-dimensional array")
    if len(arr) == 0:
        raise ValueError("Array is empty, cannot determine middle element")
    middle_index = len(arr) // 2
    return arr[middle_index]

if __name__ == '__main__':
    sample_arr = np.array([1, 2, 3, 4, 5])
    print(get_middle_element(sample_arr))