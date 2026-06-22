import numpy as np

def validate_arrays(arr1, arr2):
    if not (isinstance(arr1, list) and isinstance(arr2, list)):
        raise ValueError("Both inputs must be lists.")
    if not all(isinstance(x, int) for x in arr1 + arr2):
        raise ValueError("All elements in both lists must be integers.")
    if len(arr1) != len(arr2):
        raise ValueError("Both lists must have the same length.")

def abs_diff_arrays(arr1, arr2):
    validate_arrays(arr1, arr2)
    return np.abs(np.array(arr1) - np.array(arr2))

if __name__ == '__main__':
    sample_arr1 = [10, 5, 20, 15, 8]
    sample_arr2 = [3, 7, 18, 10, 5]
    print(abs_diff_arrays(sample_arr1, sample_arr2))