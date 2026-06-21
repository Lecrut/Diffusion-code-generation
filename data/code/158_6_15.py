import numpy as np

def filter_even_numpy(arr):
    return arr[arr % 2 == 0]

if __name__ == '__main__':
    sample_array = np.array(range(1, 21))
    even_numbers = filter_even_numpy(sample_array)
    print(even_numbers)