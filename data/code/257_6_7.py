import numpy as np

def calculate_absolute_difference(arr1, arr2):
    return np.abs(np.array(arr1) - np.array(arr2))

if __name__ == '__main__':
    sample_arr1 = [1, 2, 3]
    sample_arr2 = [4, 5, 6]
    result = calculate_absolute_difference(sample_arr1, sample_arr2)
    print(result)