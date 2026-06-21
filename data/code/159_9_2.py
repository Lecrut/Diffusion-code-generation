import numpy as np

def filter_odd_numbers(arr):
    return arr[arr % 2 != 0]

if __name__ == '__main__':
    sample_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    odd_numbers = filter_odd_numbers(sample_array)
    print(odd_numbers)