import numpy as np

def compare_arrays(arr1, arr2):
    diff_matrix = np.abs(arr1 - arr2)
    sum_squared_errors = np.sum(diff_matrix ** 2)
    return diff_matrix, sum_squared_errors

if __name__ == '__main__':
    sample_arr1 = np.array([1.0, 2.5, 3.7, 4.1])
    sample_arr2 = np.array([1.2, 2.3, 3.9, 4.0])
    diff_matrix, sum_squared_errors = compare_arrays(sample_arr1, sample_arr2)
    print("Difference Matrix:\n", diff_matrix)
    print("Sum of Squared Errors:", sum_squared_errors)