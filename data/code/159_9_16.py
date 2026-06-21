import numpy as np

def filter_odd_numbers(arr):
    return arr[arr % 2 != 0]

if __name__ == '__main__':
    sample_array = np.array([1, 3, 5, 7, 9, 11, 13])
    odd_elements = filter_odd_numbers(sample_array)
    print(odd_elements)