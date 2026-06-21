import numpy as np

def compute_average(arr):
    if not isinstance(arr, np.ndarray) or arr.dtype != np.float64:
        raise ValueError("Input must be a numpy array of floats")
    
    return np.mean(arr)

if __name__ == '__main__':
    sample_array = np.array([1.0, 2.0, 3.0, 4.0, 5.0], dtype=np.float64)
    print(compute_average(sample_array))