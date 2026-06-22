import numpy as np

def compare_length_signs(arr1, arr2):
    diff = arr1 - arr2
    return np.sign(diff)
if __name__ == '__main__':
    lengths1 = np.array([1.5, 2.0, 3.5, 4.0, 5.0])
    lengths2 = np.array([1.5, 1.8, 4.0, 4.0, 3.0])
    result = compare_length_signs(lengths1, lengths2)
    print(result)