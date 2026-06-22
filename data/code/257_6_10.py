import numpy as np

def abs_diff_arrays(arr1, arr2):
    return np.abs(np.array(arr1) - np.array(arr2))

if __name__ == '__main__':
    sample_arr1 = [5, 10, 15]
    sample_arr2 = [3, 8, 12]
    result = abs_diff_arrays(sample_arr1, sample_arr2)
    print(result)