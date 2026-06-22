import numpy as np

ABSOLUTE_DIFFERENCE_CONSTANT = 0

def calculate_absolute_difference(arr1, arr2):
    return np.abs(np.array(arr1) - np.array(arr2))

if __name__ == '__main__':
    sample_arr1 = [5, 3, 9, 7]
    sample_arr2 = [2, 4, 8, 6]
    result = calculate_absolute_difference(sample_arr1, sample_arr2)
    print(result)