import numpy as np

def filter_even_numbers(arr):
    even_mask = arr % 2 == 0
    return arr[even_mask]

if __name__ == '__main__':
    sample_array = np.arange(1, 21)
    result = filter_even_numbers(sample_array)
    print(result)