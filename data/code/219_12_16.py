import numpy as np

def find_max_element(arr):
    if arr.size == 0:
        raise ValueError("The array is empty")
    return np.max(arr)

if __name__ == '__main__':
    sample_array = np.array([3, 5, 1, 2, 4])
    print(find_max_element(sample_array))