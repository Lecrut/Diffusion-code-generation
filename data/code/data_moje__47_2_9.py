import numpy as np

def compute_mean(dataset):
    if not isinstance(dataset, (list, tuple, np.ndarray)):
        raise TypeError("Input must be a list, tuple, or numpy array")
    if len(dataset) == 0:
        raise ValueError("Dataset must not be empty")
    try:
        array_data = np.array(dataset, dtype=float)
    except (ValueError, TypeError) as e:
        raise TypeError("All elements in the dataset must be numeric") from e
    return np.mean(array_data)

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = compute_mean(sample_data)
    print(result)