import numpy as np

def safe_divide(arr1, arr2):
    result = np.where(arr2 != 0, arr1 / arr2, 0)
    return result

if __name__ == '__main__':
    array1 = np.array([10, 5, 3, 0])
    array2 = np.array([2, 0, 1, 0])
    print(safe_divide(array1, array2))