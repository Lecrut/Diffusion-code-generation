import numpy as np

def compare_arrays(array1, array2):
    difference_matrix = np.abs(array1 - array2)
    sum_of_squared_errors = np.sum(difference_matrix ** 2)
    return difference_matrix, sum_of_squared_errors

if __name__ == '__main__':
    sample_array1 = np.array([1, 2, 3, 4, 5])
    sample_array2 = np.array([4, 5, 6, 7, 8])
    diff_mat, sse = compare_arrays(sample_array1, sample_array2)
    print("Difference Matrix:")
    print(diff_mat)
    print("Sum of Squared Errors:")
    print(sse)