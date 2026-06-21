import numpy as np
MEAN_CALCULATION_THRESHOLD = 10 ** 6

def compute_average(arr):
    return np.mean(arr)
if __name__ == '__main__':
    sample_array = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    print(compute_average(sample_array))