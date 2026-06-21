import numpy as np

def filter_odd_numbers(arr):
    return arr[arr % 2 != 0]

if __name__ == '__main__':
    sample_array = np.array([13, 24, 35, 46, 57])
    filtered_odds = filter_odd_numbers(sample_array)
    print(filtered_odds)