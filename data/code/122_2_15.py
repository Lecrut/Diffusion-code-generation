import numpy as np

def average_of_floats(arr):
    return np.mean(arr, where=np.isfinite(arr), initial=0)

if __name__ == '__main__':
    sample_array = np.array([1.5, 2.5, 3.5, np.inf])
    print(average_of_floats(sample_array))