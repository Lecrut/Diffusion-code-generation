import numpy as np

def calculate_average_pairs(arr):
    if len(arr) % 2 != 0:
        raise ValueError("Array length must be even")
    pairs = arr.reshape(-1, 2)
    averages = np.mean(pairs, axis=1)
    return averages

if __name__ == '__main__':
    sample_array = np.array([1, 2, 3, 4, 5, 6])
    result = calculate_average_pairs(sample_array)
    print(result)