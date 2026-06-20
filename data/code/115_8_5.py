import numpy as np

def safe_divide(a, b):
    result = np.where(b == 0, 0, a / b)
    return result

if __name__ == '__main__':
    array1 = np.array([10, 20, 30, 40])
    array2 = np.array([2, 4, 0, 8])
    print(safe_divide(array1, array2))