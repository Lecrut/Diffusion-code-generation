import numpy as np

def filter_even_numpy(arr):
    return arr[arr % 2 == 0]

if __name__ == '__main__':
    sample_array = np.array([1, 3, 5, 7, 9, 10, 12, 14, 16, 18, 20])
    result = filter_even_numpy(sample_array)
    print(result)