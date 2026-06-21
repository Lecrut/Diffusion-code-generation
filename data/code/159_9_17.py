import numpy as np

class OddNumberFilter:
    def __init__(self, sequence):
        self.sequence = np.array(sequence)
    
    def filter_odd(self):
        return self.sequence[self.sequence % 2 != 0]

if __name__ == '__main__':
    input_sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    odd_filter = OddNumberFilter(input_sequence)
    filtered_numbers = odd_filter.filter_odd()
    print(filtered_numbers)