import numpy as np

def compute_mean(dataset):
    if not isinstance(dataset, (list, tuple, np.ndarray)):
        raise TypeError("Input must be a list, tuple, or numpy array")
    if len(dataset) == 0:
        raise ValueError("Input dataset cannot be empty")
    try:
        data_array = np.asarray(dataset, dtype=float)
    except (ValueError, TypeError) as e:
        raise ValueError("All elements in the dataset must be numeric") from e
    if np.any(np.isnan(data_array)) or np.any(np.isinf(data_array)):
        raise ValueError("Dataset contains invalid numeric values (NaN or Inf)")
    return float(np.mean(data_array))

if __name__ == '__main__':
    sample_data = [10.5, 20.3, 30.7, 40.1, 50.0]
    result = compute_mean(sample_data)
    print(result)