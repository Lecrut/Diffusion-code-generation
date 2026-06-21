import numpy as np

def extract_initial_value(array):
    if not isinstance(array, np.ndarray):
        raise ValueError("Input must be a NumPy array")
    if array.size == 0:
        raise ValueError("Array is empty")
    return array.flat[0]

if __name__ == '__main__':
    sample_array = np.array([[1, 2, 3], [4, 5, 6]])
    result = extract_initial_value(sample_array)
    print(result)