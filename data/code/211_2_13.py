import numpy as np

def compare_arrays(arr1, arr2):
    if not isinstance(arr1, np.ndarray) or not isinstance(arr2, np.ndarray):
        raise ValueError("Both inputs must be numpy arrays.")
    
    diff_matrix = np.abs(arr1 - arr2)
    sum_squared_errors = np.sum(diff_matrix**2)
    
    return diff_matrix, sum_squared_errors

if __name__ == '__main__':
    sample_arr1 = np.array([1, 2, 3, 4, 5])
    sample_arr2 = np.array([4, 5, 6, 7, 8])
    
    try:
        result_matrix, error_sum = compare_arrays(sample_arr1, sample_arr2)
        print("Difference Matrix:")
        print(result_matrix)
        print("Sum of Squared Errors:")
        print(error_sum)
    except ValueError as e:
        print(e)