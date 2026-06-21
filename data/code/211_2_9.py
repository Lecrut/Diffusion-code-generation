import numpy as np

def compare_arrays(arr1, arr2):
    abs_diff = np.abs(arr1 - arr2)
    sum_squared_errors = np.sum(np.square(abs_diff))
    return abs_diff, sum_squared_errors

if __name__ == '__main__':
    sample_arr1 = np.array([1, 2, 3])
    sample_arr2 = np.array([4, 5, 6])
    result = compare_arrays(sample_arr1, sample_arr2)
    print("Absolute Difference Matrix:")
    print(result[0])
    print("Sum of Squared Errors:", result[1])