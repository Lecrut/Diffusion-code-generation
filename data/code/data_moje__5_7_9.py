import numpy as np

def compare_length_signs(arr1, arr2):
    a = np.asarray(arr1, dtype=float)
    b = np.asarray(arr2, dtype=float)
    return np.sign(a - b)

if __name__ == '__main__':
    lengths1 = [10.5, 20.0, 15.3, 8.7, 25.1]
    lengths2 = [10.5, 18.0, 15.3, 9.0, 20.0]
    result = compare_length_signs(lengths1, lengths2)
    print(result)