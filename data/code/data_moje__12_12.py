import numpy as np

def get_middle_element(arr):
    if arr.ndim != 1:
        raise ValueError("Input must be a 1-dimensional array")
    if arr.size == 0:
        raise ValueError("Array must not be empty")
    mid_index = arr.size // 2
    if arr.size % 2 == 1:
        return arr[mid_index]
    else:
        return arr[mid_index]

if __name__ == '__main__':
    sample_odd = np.array([1, 2, 3, 4, 5])
    sample_even = np.array([1, 2, 3, 4])
    print(get_middle_element(sample_odd))
    print(get_middle_element(sample_even))