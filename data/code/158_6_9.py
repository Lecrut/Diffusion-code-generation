import numpy as np

def filter_even_numpy(array):
    return array[array % 2 == 0]

if __name__ == '__main__':
    sample_array = np.arange(1, 21)
    even_numbers = filter_even_numpy(sample_array)
    print(even_numbers)