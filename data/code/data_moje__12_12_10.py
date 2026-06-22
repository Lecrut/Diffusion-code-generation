import numpy as np

def get_middle_element(arr):
    arr = np.asarray(arr)
    if arr.ndim != 1:
        raise ValueError("Input must be a 1-dimensional array.")
    if arr.size == 0:
        raise ValueError("Cannot get middle element of an empty array.")
    return arr[arr.size // 2]

if __name__ == '__main__':
    data = np.array([10, 20, 30, 40, 50])
    result = get_middle_element(data)
    print(result)