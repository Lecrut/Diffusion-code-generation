import numpy as np
DIVISION_TOLERANCE = 1e-08

def safe_divide(a, b):
    a = np.array(a)
    b = np.array(b)
    non_zero_mask = np.abs(b) > DIVISION_TOLERANCE
    result = np.zeros_like(b)
    result[non_zero_mask] = a[non_zero_mask] / b[non_zero_mask]
    return result
if __name__ == '__main__':
    array1 = np.array([10, 20, 30, 40])
    array2 = np.array([2, 0, 5, 0])
    division_result = safe_divide(array1, array2)
    print(division_result)