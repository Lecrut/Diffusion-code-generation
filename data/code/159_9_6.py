import numpy as np

def filter_odd_numbers(arr):
    return arr[arr % 2 != 0]

if __name__ == '__main__':
    input_sequence = np.array([10, 23, 45, 67, 89, 2, 4, 6, 8])
    odd_numbers = filter_odd_numbers(input_sequence)
    print(odd_numbers)