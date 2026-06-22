import numpy as np

def find_max_element(arr):
    return np.max(arr)

if __name__ == '__main__':
    sample_array = np.array([3, 5, 2, 8, 1])
    print(find_max_element(sample_array))