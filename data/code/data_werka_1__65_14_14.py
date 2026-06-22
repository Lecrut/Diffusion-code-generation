import numpy as np

def extract_elements(array, indices):
    if not isinstance(array, np.ndarray) or not isinstance(indices, np.ndarray):
        raise ValueError("Both array and indices must be NumPy arrays.")
    return array[indices]

if __name__ == '__main__':
    sample_array = np.array([10, 20, 30, 40, 50])
    sample_indices = np.array([0, 2, 4])
    result = extract_elements(sample_array, sample_indices)
    print(result)