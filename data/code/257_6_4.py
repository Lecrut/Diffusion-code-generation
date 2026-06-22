import numpy as np

def calculate_absolute_difference(arr1, arr2):
    return np.abs(np.subtract(arr1, arr2))

if __name__ == '__main__':
    array1 = np.array([1, 2, 3, 4, 5])
    array2 = np.array([5, 4, 3, 2, 1])
    result = calculate_absolute_difference(array1, array2)
    print(result)