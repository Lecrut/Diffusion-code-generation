import numpy as np

def compare_lengths(arr1, arr2):
    arr1 = np.asarray(arr1)
    arr2 = np.asarray(arr2)
    diff = arr1 - arr2
    sign = np.sign(diff)
    return sign

if __name__ == '__main__':
    sample_a = np.array([10.5, 20.0, 15.3, 8.1])
    sample_b = np.array([10.5, 18.2, 16.0, 8.1])
    result = compare_lengths(sample_a, sample_b)
    print(result)