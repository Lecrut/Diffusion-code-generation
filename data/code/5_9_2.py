import numpy as np
def compare_signs(arr1, arr2):
    return np.sign(arr1 - arr2)
if __name__ == '__main__':
    arr_a = np.array([1.0, 5.5, -3.0, 0.0, 10.2])
    arr_b = np.array([1.1, 5.4, -3.1, 0.1, 10.3])
    result = compare_signs(arr_a, arr_b)
    print(result)