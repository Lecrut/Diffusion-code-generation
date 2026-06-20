import numpy as np

def vectorized_divide(arr1, arr2):
    return np.where(arr2 != 0, arr1 / arr2, 0)
if __name__ == '__main__':
    sample_arr1 = np.array([50, 60, 70, 80])
    sample_arr2 = np.array([2, 3, 0, 4])
    result = vectorized_divide(sample_arr1, sample_arr2)
    print(result)