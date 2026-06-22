import numpy as np

def find_max_value(arr):
    return np.max(arr)

if __name__ == '__main__':
    sample_array = np.array([3, 5, 1, 2, 4])
    print(find_max_value(sample_array))