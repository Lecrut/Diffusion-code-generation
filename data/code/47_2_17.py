import numpy as np

def calculate_mean(data):
    if not isinstance(data, (list, tuple, np.ndarray)):
        raise TypeError("Input must be a list, tuple, or NumPy array.")
    if len(data) == 0:
        raise ValueError("Input data cannot be empty.")
    try:
        arr = np.array(data)
        if not np.issubdtype(arr.dtype, np.number):
            raise TypeError("All elements in the input data must be numeric.")
        return np.mean(arr)
    except (TypeError, ValueError) as e:
        raise e

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = calculate_mean(sample_data)
    print(result)