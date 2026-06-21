import numpy as np

def get_middle_element(arr):
    if arr.ndim != 1:
        raise ValueError("Input must be a 1-dimensional array")
    mid_index = len(arr) // 2
    return arr[mid_index]

if __name__ == '__main__':
    sample_array1 = np.array([1, 2, 3, 4, 5])
    sample_array2 = np.array([10, 20, 30])
    print(get_middle_element(sample_array1))
    print(get_middle_element(sample_array2))