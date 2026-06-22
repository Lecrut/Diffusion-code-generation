import numpy as np

def calculate_average_of_pairs(arr):
    return np.array([np.mean(pair) for pair in arr])

if __name__ == '__main__':
    sample_array = [[1, 2], [3, 4], [5, 6]]
    result = calculate_average_of_pairs(sample_array)
    print(result)