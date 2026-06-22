import numpy as np

def compute_mean(data):
    if not isinstance(data, (list, tuple, np.ndarray)):
        raise TypeError("Input data must be a list, tuple, or NumPy array")
    if len(data) == 0:
        raise ValueError("Input data must not be empty")
    try:
        np_data = np.asarray(data, dtype=float)
    except (TypeError, ValueError) as e:
        raise ValueError("All elements in input data must be numeric") from e
    return float(np.mean(np_data))

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = compute_mean(sample_data)
    print(result)