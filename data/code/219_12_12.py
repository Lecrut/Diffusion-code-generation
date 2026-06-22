import numpy as np

def find_max_numpy(arr):
    if arr.size == 0:
        raise ValueError("The array is empty")
    return np.amax(arr)

if __name__ == '__main__':
    sample_array = np.array([3, 5, 1, 8, 2, 9, 4])
    print(find_max_numpy(sample_array))