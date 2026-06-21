import numpy as np

def compute_average(arr):
    return np.mean(arr)

if __name__ == '__main__':
    sample_array = np.array([3.5, 2.8, 4.1, 5.0, 3.9])
    print(compute_average(sample_array))