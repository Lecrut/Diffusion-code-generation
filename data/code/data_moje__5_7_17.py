import numpy as np

def compare_lengths(array1, array2):
    arr1 = np.asarray(array1, dtype=np.float64)
    arr2 = np.asarray(array2, dtype=np.float64)
    return np.sign(arr1 - arr2)

if __name__ == '__main__':
    a = [1.5, 2.0, 3.5, 4.0, 5.0]
    b = [1.0, 2.5, 3.5, 4.0, 4.5]
    result = compare_lengths(a, b)
    print(result)