import numpy as np

def compute_average(arr):
    return np.mean(arr)

if __name__ == '__main__':
    sample_array = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    average = compute_average(sample_array)
    print(average)