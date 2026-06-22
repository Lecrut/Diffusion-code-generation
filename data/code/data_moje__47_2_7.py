import numpy as np

def compute_mean(data):
    if not isinstance(data, (list, tuple, np.ndarray)):
        raise TypeError("Input must be a list, tuple, or numpy array")
    if len(data) == 0:
        raise ValueError("Input data must not be empty")
    try:
        numeric_data = [float(x) for x in data]
    except (TypeError, ValueError):
        raise TypeError("All elements in the input must be numeric")
    return float(np.mean(numeric_data))

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = compute_mean(sample_data)
    print(result)