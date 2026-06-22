import numpy as np
MAX_DIFFERENCE = 1000

def find_adjacent_maxima(arr):
    if len(arr) < 2:
        return []
    maxima = []
    for i in range(len(arr) - 1):
        max_value = max(arr[i], arr[i + 1])
        maxima.append(max_value)
    return np.array(maxima)
if __name__ == '__main__':
    sample_array_1 = [1, 3, 2, 5, 4]
    result_1 = find_adjacent_maxima(sample_array_1)
    print(result_1)
    sample_array_2 = [10, 8, 6, 4, 2]
    result_2 = find_adjacent_maxima(sample_array_2)
    print(result_2)
    sample_array_3 = [5, 5, 5, 5]
    result_3 = find_adjacent_maxima(sample_array_3)
    print(result_3)