import numpy as np

def compare_lengths(array1, array2):
    return np.sign(array1 - array2)

if __name__ == '__main__':
    array1 = np.array([10.5, 20.3, 30.7])
    array2 = np.array([10.0, 20.3, 40.0])
    result = compare_lengths(array1, array2)
    print(result)