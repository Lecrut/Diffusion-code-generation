import numpy as np

def compute_mean(arr):
    return np.mean(arr)

if __name__ == '__main__':
    sample_array = np.array([10, 20, 30, 40, 50])
    print(compute_mean(sample_array))