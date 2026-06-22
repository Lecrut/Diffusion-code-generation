import numpy as np

def extract_elements(array, indices):
    if not isinstance(array, np.ndarray) or not isinstance(indices, np.ndarray):
        raise ValueError("Both array and indices must be NumPy arrays.")
    return array[indices]

if __name__ == '__main__':
    sample_array = np.array([100, 200, 300, 400, 500])
    sample_indices = np.array([1, 3])
    result = extract_elements(sample_array, sample_indices)
    print(result)