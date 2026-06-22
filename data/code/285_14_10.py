import numpy as np

def compare_adjacent_elements(arr):
    return np.maximum(arr[:-1], arr[1:])

if __name__ == '__main__':
    sample_array = np.array([3, 5, 2, 8, 6])
    result = compare_adjacent_elements(sample_array)
    print(result)