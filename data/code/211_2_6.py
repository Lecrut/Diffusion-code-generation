import numpy as np

def compare_arrays(arr1, arr2):
    diff_matrix = np.abs(arr1 - arr2)
    sum_squared_errors = np.sum(diff_matrix ** 2)
    return diff_matrix, sum_squared_errors

if __name__ == '__main__':
    sample_arr1 = np.array([1, 2, 3])
    sample_arr2 = np.array([4, 5, 6])
    diff_matrix, sum_squared_errors = compare_arrays(sample_arr1, sample_arr2)
    print("Difference Matrix:")
    print(diff_matrix)
    print("Sum of Squared Errors:", sum_squared_errors)