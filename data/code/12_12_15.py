import numpy as np

def get_middle_element(arr):
    if arr.ndim != 1:
        raise ValueError("Input must be a 1-dimensional numpy array")
    mid_index = len(arr) // 2
    return arr[mid_index]

if __name__ == '__main__':
    sample_array = np.array([1, 2, 3, 4, 5])
    print(get_middle_element(sample_array))