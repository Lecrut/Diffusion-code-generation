import numpy as np

def compute_mean(arr):
    return np.mean(arr)

if __name__ == '__main__':
    sample_array = np.array([1, 2, 3, 4, 5], dtype=np.float64)
    print(compute_mean(sample_array))