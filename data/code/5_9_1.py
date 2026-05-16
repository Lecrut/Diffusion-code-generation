import numpy as np
def compare_signs(arr1, arr2):
    return np.sign(arr1 - arr2)
if __name__ == '__main__':
    arr_a = np.array([10, 20, 30, 40, 50])
    arr_b = np.array([12, 18, 30, 45, 55])
    result = compare_signs(arr_a, arr_b)
    print(result)