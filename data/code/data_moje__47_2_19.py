import numpy as np

def calculate_mean(data):
    if not isinstance(data, (list, tuple, np.ndarray)):
        raise TypeError("Input data must be a list, tuple, or NumPy array.")
    if len(data) == 0:
        raise ValueError("Input data cannot be empty.")
    try:
        return float(np.mean(data))
    except (TypeError, ValueError) as e:
        raise ValueError("All elements in the input data must be numeric.") from e

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = calculate_mean(sample_data)
    print(result)