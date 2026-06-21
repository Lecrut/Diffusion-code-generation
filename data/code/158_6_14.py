import numpy as np

class ArrayFilter:
    @staticmethod
    def create_and_filter_even():
        array = np.arange(1, 21)
        even_array = array[array % 2 == 0]
        return even_array

if __name__ == '__main__':
    result = ArrayFilter.create_and_filter_even()
    print(result)