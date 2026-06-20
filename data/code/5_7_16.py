import numpy as np

def compare_length_signs(arr1, arr2):
    diff = arr1 - arr2
    return np.sign(diff)

if __name__ == '__main__':
    a = np.array([1.5, 3.0, 2.5, 4.0])
    b = np.array([2.0, 2.5, 2.5, 3.5])
    result = compare_length_signs(a, b)
    print(result)