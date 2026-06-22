import numpy as np

def calculate_mean(dataset):
    if not isinstance(dataset, (list, tuple, np.ndarray)):
        raise TypeError("Input must be a list, tuple, or numpy array")
    if len(dataset) == 0:
        raise ValueError("Dataset cannot be empty")
    try:
        converted_data = np.array(dataset, dtype=float)
    except (TypeError, ValueError):
        raise TypeError("All elements in the dataset must be numeric")
    return np.mean(converted_data)

if __name__ == '__main__':
    sample_data = [10.0, 20.0, 30.0, 40.0, 50.0]
    result = calculate_mean(sample_data)
    print(result)