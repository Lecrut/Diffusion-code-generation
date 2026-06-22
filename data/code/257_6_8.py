import numpy as np

def abs_diff_arrays(arr1, arr2):
    return np.abs(np.subtract(arr1, arr2))

if __name__ == '__main__':
    array1 = np.array([1, 2, 3])
    array2 = np.array([4, 5, 6])
    result = abs_diff_arrays(array1, array2)
    print(result)