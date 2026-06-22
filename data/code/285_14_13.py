import numpy as np

def max_adjacent_elements(arr):
    return np.maximum(arr[:-1], arr[1:])

if __name__ == '__main__':
    sample_array = np.array([3, 5, 2, 8, 6])
    result = max_adjacent_elements(sample_array)
    print(result)