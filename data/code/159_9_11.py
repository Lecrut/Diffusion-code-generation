import numpy as np

class OddNumberFilter:
    def __init__(self, array):
        self.array = np.array(array)

    def filter_odd_numbers(self):
        return self.array[self.array % 2 != 0]

if __name__ == '__main__':
    sample_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    filter_instance = OddNumberFilter(sample_array)
    odd_numbers = filter_instance.filter_odd_numbers()
    print(odd_numbers)