import numpy as np

def abs_diff_arrays(arr1, arr2):
    return np.abs(np.subtract(arr1, arr2))

if __name__ == '__main__':
    sample_arr1 = np.array([1, 2, 3])
    sample_arr2 = np.array([4, 5, 6])
    print(abs_diff_arrays(sample_arr1, sample_arr2))