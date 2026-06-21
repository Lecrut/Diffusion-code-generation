import numpy as np
ODD_THRESHOLD = 2

def filter_odd_numbers(arr):
    return arr[arr % ODD_THRESHOLD != 0]
if __name__ == '__main__':
    sample_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    result = filter_odd_numbers(sample_array)
    print(result)