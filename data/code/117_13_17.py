import numpy as np

def validate_arrays(array1, array2):
    if len(array1) != 10000 or len(array2) != 10000:
        raise ValueError("Arrays must be of length 10000")
    if not isinstance(array1, np.ndarray) or not isinstance(array2, np.ndarray):
        raise TypeError("Inputs must be NumPy arrays")

def calculate_difference():
    array1 = np.array([i for i in range(10000)])
    array2 = np.array([i * 3 for i in range(10000)])
    validate_arrays(array1, array2)
    difference = array2 - array1
    return difference

if __name__ == '__main__':
    result = calculate_difference()
    print(result)