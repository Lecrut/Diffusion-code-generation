import numpy as np

def compute_mean(data):
    if not isinstance(data, (list, tuple, np.ndarray)):
        raise TypeError("Input data must be a list, tuple, or numpy array")
    if len(data) == 0:
        raise ValueError("Input data must not be empty")
    try:
        numeric_data = [float(x) for x in data]
    except (TypeError, ValueError) as e:
        raise TypeError("All elements in input data must be numeric") from e
    array_data = np.array(numeric_data)
    return float(np.mean(array_data))

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    result = compute_mean(sample_data)
    print(result)