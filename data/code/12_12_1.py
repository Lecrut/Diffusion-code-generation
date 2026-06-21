import numpy as np

def get_middle_element(arr):
    if not isinstance(arr, np.ndarray):
        raise TypeError("Input must be a numpy array")
    if arr.ndim != 1:
        raise ValueError("Input must be a 1-dimensional array")
    if arr.size == 0:
        raise ValueError("Array must not be empty")
    return arr[arr.size // 2]

if __name__ == '__main__':
    data = np.array([10, 20, 30, 40, 50, 60, 70])
    result = get_middle_element(data)
    print(result)