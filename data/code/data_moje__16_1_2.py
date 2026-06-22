import numpy as np

def get_initial_value(arr):
    if not hasattr(arr, '__len__') or len(arr) == 0:
        raise ValueError("Array must not be empty")
    return arr.flat[0]

if __name__ == '__main__':
    sample_array = np.array([42, 15, 7, 99, 3])
    result = get_initial_value(sample_array)
    print(result)
    sample_2d = np.array([[1, 2], [3, 4]])
    result_2d = get_initial_value(sample_2d)
    print(result_2d)