import numpy as np

def compute_average(arr):
    if not isinstance(arr, np.ndarray) or arr.ndim != 1 or arr.dtype.kind != 'f':
        raise ValueError("Input must be a one-dimensional numpy array of floats.")
    return np.mean(arr)

if __name__ == '__main__':
    sample_array = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    print(compute_average(sample_array))