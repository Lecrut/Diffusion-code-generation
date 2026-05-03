import numpy as np
def compare_signs(arr1, arr2):
    return np.sign(arr1 - arr2)
if __name__ == '__main__':
    array1 = np.array([10, 5, 20, 15, 30])
    array2 = np.array([12, 4, 22, 14, 28])
    result = compare_signs(array1, array2)
    print(result)