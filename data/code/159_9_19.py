import numpy as np

def filter_odd_numbers(arr):
    return arr[arr % 2 != 0]

if __name__ == '__main__':
    sample_array = np.array([15, 33, 47, 60, 89])
    odd_numbers = filter_odd_numbers(sample_array)
    print(odd_numbers)