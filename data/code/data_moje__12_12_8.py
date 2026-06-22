import numpy as np

def get_middle_element(arr):
    if arr.ndim != 1:
        raise ValueError("Input must be a 1-dimensional array")
    if len(arr) == 0:
        raise ValueError("Input array must not be empty")
    return arr[len(arr) // 2]

if __name__ == '__main__':
    sample_array = np.array([10, 20, 30, 40, 50])
    print(get_middle_element(sample_array))
    sample_array_even = np.array([1, 2, 3, 4])
    print(get_middle_element(sample_array_even))