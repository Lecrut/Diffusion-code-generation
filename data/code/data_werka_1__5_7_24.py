import numpy as np

def compare_lengths(arr1, arr2):
    return np.sign(arr1 - arr2)

if __name__ == '__main__':
    sample_arr1 = np.array([10, 20, 30, 40])
    sample_arr2 = np.array([5, 25, 30, 35])
    result = compare_lengths(sample_arr1, sample_arr2)
    print(result)