import numpy as np

def abs_diff_arrays(arr1, arr2):
    return np.abs(np.array(arr1) - np.array(arr2))

if __name__ == '__main__':
    sample_arr1 = [10, 5, 20, 15, 8]
    sample_arr2 = [3, 7, 14, 25, 6]
    result = abs_diff_arrays(sample_arr1, sample_arr2)
    print(result)