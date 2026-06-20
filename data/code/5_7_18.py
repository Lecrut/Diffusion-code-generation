import numpy as np

def compare_lengths(arr1, arr2):
    diff = np.asarray(arr1) - np.asarray(arr2)
    return np.sign(diff)

if __name__ == '__main__':
    a = np.array([10.5, 5.0, 8.2, 12.1, 3.4])
    b = np.array([10.5, 6.0, 8.2, 11.0, 4.0])
    result = compare_lengths(a, b)
    print(result)