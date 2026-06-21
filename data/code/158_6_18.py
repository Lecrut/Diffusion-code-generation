import numpy as np

class ArrayFilter:
    @staticmethod
    def filter_even(numbers):
        return numbers[numbers % 2 == 0]

if __name__ == '__main__':
    sample_array = np.array(range(1, 21))
    even_numbers = ArrayFilter.filter_even(sample_array)
    print(even_numbers)