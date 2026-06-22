import numpy as np

def average_pairs(arr):
    return np.array([np.mean(pair) for pair in zip(arr[:-1], arr[1:])])

if __name__ == '__main__':
    sample_array = np.array([1, 2, 3, 4, 5])
    result = average_pairs(sample_array)
    print(result)