import numpy as np

def find_adjacent_maxima(arr):
    if not isinstance(arr, np.ndarray) or len(arr) < 2:
        raise ValueError("Input must be a numpy array with at least two elements")
    
    maxima = np.maximum.accumulate(arr)
    shifted_maxima = np.roll(maxima, -1)
    adjacent_maxima = np.maximum(maxima, shifted_maxima)
    
    return adjacent_maxima[:-1]

if __name__ == '__main__':
    sample_array_1 = np.array([1, 3, 2, 5, 4])
    result_1 = find_adjacent_maxima(sample_array_1)
    print(result_1)
    
    sample_array_2 = np.array([10, 8, 6, 4, 2])
    result_2 = find_adjacent_maxima(sample_array_2)
    print(result_2)
    
    sample_array_3 = np.array([5, 5, 5, 5])
    result_3 = find_adjacent_maxima(sample_array_3)
    print(result_3)