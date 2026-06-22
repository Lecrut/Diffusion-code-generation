import numpy as np

def compute_mean(data):
    if not isinstance(data, (list, tuple, np.ndarray)):
        raise TypeError("Input must be a list, tuple, or NumPy array")
    if len(data) == 0:
        raise ValueError("Input dataset cannot be empty")
    for item in data:
        if not isinstance(item, (int, float, np.integer, np.floating)):
            raise TypeError("All elements must be numeric")
    array_data = np.array(data, dtype=float)
    return np.mean(array_data)

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    result = compute_mean(sample_data)
    print(result)