import numpy as np

def calculate_abs_difference(arr1, arr2):
    arr1_np = np.array(arr1)
    arr2_np = np.array(arr2)
    return np.abs(arr1_np - arr2_np)

if __name__ == '__main__':
    sample_arr1 = [5, 3, 9, 7]
    sample_arr2 = [8, 6, 4, 2]
    result = calculate_abs_difference(sample_arr1, sample_arr2)
    print(result)