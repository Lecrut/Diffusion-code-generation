import numpy as np

def compare_lengths(arr1, arr2):
    return np.sign(arr1 - arr2)

if __name__ == '__main__':
    sample_array1 = np.array([5.0, 3.2, 7.8, 6.4])
    sample_array2 = np.array([4.9, 3.2, 7.9, 6.0])
    result = compare_lengths(sample_array1, sample_array2)
    print(result)