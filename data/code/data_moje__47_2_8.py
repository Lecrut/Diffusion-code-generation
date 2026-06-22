import numpy as np

def compute_mean(data):
    if not isinstance(data, (list, tuple, np.ndarray)):
        raise TypeError("Input must be a list, tuple, or NumPy array")
    if len(data) == 0:
        raise ValueError("Input dataset cannot be empty")
    try:
        data_array = np.asarray(data, dtype=float)
    except (ValueError, TypeError) as e:
        raise TypeError("All elements in the dataset must be numeric") from e
    return float(np.mean(data_array))

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = compute_mean(sample_data)
    print(result)