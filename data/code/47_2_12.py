import numpy as np

def compute_mean(dataset):
    if not isinstance(dataset, (list, tuple, np.ndarray)):
        raise TypeError("Dataset must be a list, tuple, or numpy array")
    if len(dataset) == 0:
        raise ValueError("Dataset must not be empty")
    try:
        data_array = np.array(dataset, dtype=float)
    except (ValueError, TypeError) as e:
        raise ValueError("All elements in dataset must be numeric") from e
    return float(np.mean(data_array))

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = compute_mean(sample_data)
    print(result)