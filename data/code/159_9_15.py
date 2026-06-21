import numpy as np

def filter_odd_numbers(sequence):
    if not isinstance(sequence, (list, np.ndarray)) or not all((isinstance(item, int) for item in sequence)):
        raise ValueError('Input must be a list or numpy array of integers.')
    return sequence[sequence % 2 != 0]
if __name__ == '__main__':
    input_sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    odd_numbers = filter_odd_numbers(input_sequence)
    print(odd_numbers)