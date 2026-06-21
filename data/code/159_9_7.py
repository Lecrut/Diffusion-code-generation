import numpy as np

def filter_odd_numbers(arr):
    return arr[arr % 2 != 0]

if __name__ == '__main__':
    sample_array = np.array([11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
    odd_numbers = filter_odd_numbers(sample_array)
    print(odd_numbers)