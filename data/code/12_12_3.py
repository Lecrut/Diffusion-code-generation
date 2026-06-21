import numpy as np

def get_middle_element(arr):
    if not isinstance(arr, np.ndarray):
        raise TypeError("Input must be a numpy array")
    if arr.ndim != 1:
        raise ValueError("Input must be a 1-dimensional array")
    return arr[len(arr) // 2]

if __name__ == '__main__':
    sample_array = np.array([10, 20, 30, 40, 50])
    middle_val = get_middle_element(sample_array)
    print(middle_val)