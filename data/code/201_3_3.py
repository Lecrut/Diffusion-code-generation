import numpy as np

def average_numpy_array(arr):
    return np.mean(arr)

if __name__ == '__main__':
    sample_array = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    print(average_numpy_array(sample_array))