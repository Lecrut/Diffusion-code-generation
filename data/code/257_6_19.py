import numpy as np

def abs_diff_arrays(arr1, arr2):
    return np.abs(np.array(arr1) - np.array(arr2))

if __name__ == '__main__':
    array1 = [10, 20, 30, 40]
    array2 = [5, 15, 25, 35]
    result = abs_diff_arrays(array1, array2)
    print(result)