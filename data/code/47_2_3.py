import numpy as np

def compute_mean(dataset):
    if not isinstance(dataset, (list, tuple, np.ndarray)):
        raise TypeError("Input must be a list, tuple, or NumPy array.")
    if len(dataset) == 0:
        raise ValueError("Input dataset must not be empty.")
    try:
        np_array = np.array(dataset, dtype=float)
    except (ValueError, TypeError) as e:
        raise ValueError("All elements in the dataset must be numeric.") from e
    if np.any(np.isnan(np_array)):
        raise ValueError("Dataset contains NaN values.")
    return np.mean(np_array)

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = compute_mean(sample_data)
    print(result)