import numpy as np

def abs_diff_arrays(arr1, arr2):
    return np.abs(np.array(arr1) - np.array(arr2))

if __name__ == '__main__':
    sample_arr1 = [3, 9, 5]
    sample_arr2 = [1, 7, 6]
    result = abs_diff_arrays(sample_arr1, sample_arr2)
    print(result)