import numpy as np

def filter_even_numpy(arr):
    return arr[arr % 2 == 0]

if __name__ == '__main__':
    sample_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    result = filter_even_numpy(sample_array)
    print(result)