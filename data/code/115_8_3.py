import numpy as np

def safe_divide(a, b):
    result = np.zeros_like(b)
    non_zero_mask = b != 0
    result[non_zero_mask] = a[non_zero_mask] / b[non_zero_mask]
    return result

if __name__ == '__main__':
    array1 = np.array([15, 25, 35, 45])
    array2 = np.array([2, 0, 5, 0])
    division_result = safe_divide(array1, array2)
    print(division_result)