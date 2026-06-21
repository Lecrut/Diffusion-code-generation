import numpy as np

def validate_arrays(array1, array2):
    if not (isinstance(array1, np.ndarray) and isinstance(array2, np.ndarray)):
        raise ValueError("Both inputs must be numpy arrays.")
    if array1.shape != array2.shape:
        raise ValueError("Arrays must have the same shape.")

def calculate_absolute_difference(array1, array2):
    validate_arrays(array1, array2)
    return np.abs(array1 - array2)

def sum_of_squared_errors(array1, array2):
    validate_arrays(array1, array2)
    difference = array1 - array2
    return np.sum(difference ** 2)

if __name__ == '__main__':
    sample_array1 = np.array([1, 2, 3])
    sample_array2 = np.array([4, 5, 6])
    absolute_difference = calculate_absolute_difference(sample_array1, sample_array2)
    squared_error_sum = sum_of_squared_errors(sample_array1, sample_array2)
    print("Absolute Difference Matrix:")
    print(absolute_difference)
    print("Sum of Squared Errors:")
    print(squared_error_sum)