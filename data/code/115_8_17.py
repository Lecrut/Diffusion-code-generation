import numpy as np

def validate_arrays(a, b):
    if a.shape != b.shape:
        raise ValueError("Arrays must have identical shapes")

def elementwise_divide(a, b):
    validate_arrays(a, b)
    result = np.where(b != 0, a / b, 0)
    return result

if __name__ == '__main__':
    array1 = np.array([10, 20, 30, 40])
    array2 = np.array([2, 0, 5, 0])
    division_result = elementwise_divide(array1, array2)
    print(division_result)