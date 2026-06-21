import numpy as np

class ArrayFilter:
    @staticmethod
    def filter_even_numbers(arr):
        return arr[arr % 2 == 0]

if __name__ == '__main__':
    sample_array = np.array(range(1, 21))
    even_numbers = ArrayFilter.filter_even_numbers(sample_array)
    print(even_numbers)