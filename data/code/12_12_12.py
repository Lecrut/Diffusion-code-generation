import numpy as np

def get_middle_element(arr):
    arr = np.asarray(arr)
    if arr.ndim != 1:
        raise ValueError("Input must be a 1-dimensional array")
    return arr[arr.shape[0] // 2]

if __name__ == '__main__':
    sample_array = np.array([10, 20, 30, 40, 50])
    result = get_middle_element(sample_array)
    print(result)