import numpy as np

def compare_length_signs(arr1, arr2):
    arr1 = np.asarray(arr1, dtype=np.float64)
    arr2 = np.asarray(arr2, dtype=np.float64)
    return np.sign(arr1 - arr2)
if __name__ == '__main__':
    sample_arr1 = np.array([1.5, 2.0, 3.5, 4.0, 5.5])
    sample_arr2 = np.array([1.0, 2.5, 3.5, 3.0, 6.0])
    result = compare_length_signs(sample_arr1, sample_arr2)
    print(result)