import numpy as np

def safe_divide(a, b):
    result = np.where(b != 0, a / b, 0)
    return result

if __name__ == '__main__':
    array1 = np.array([10, 20, 30, 40])
    array2 = np.array([2, 0, 5, 8])
    print(safe_divide(array1, array2))