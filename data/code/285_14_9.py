import numpy as np

def compare_adjacent_elements(arr):
    return np.maximum(arr[:-1], arr[1:])

if __name__ == '__main__':
    sample_array = np.array([1, 3, 2, 5, 4])
    result = compare_adjacent_elements(sample_array)
    print(result)