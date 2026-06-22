import numpy as np

def get_middle_element(arr):
    if arr.ndim != 1:
        raise ValueError("Input must be a 1-dimensional array.")
    if arr.size == 0:
        raise ValueError("Input array must not be empty.")
    mid_index = arr.size // 2
    if arr.size % 2 == 0:
        return arr[mid_index]
    return arr[mid_index]

if __name__ == '__main__':
    sample_array_odd = np.array([1, 2, 3, 4, 5])
    sample_array_even = np.array([10, 20, 30, 40])
    result_odd = get_middle_element(sample_array_odd)
    result_even = get_middle_element(sample_array_even)
    print(result_odd)
    print(result_even)