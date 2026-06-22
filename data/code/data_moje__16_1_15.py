import numpy as np

def extract_initial_value(arr):
    if not isinstance(arr, np.ndarray):
        raise TypeError('Input must be a NumPy array')
    if arr.size == 0:
        raise ValueError('Input array is empty')
    return arr.flat[0]
if __name__ == '__main__':
    sample_array = np.array([1, 2, 3, 4, 5])
    initial_value = extract_initial_value(sample_array)
    print(initial_value)