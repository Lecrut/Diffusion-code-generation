import numpy as np

def calculate_mean(data):
    if not isinstance(data, (list, tuple, np.ndarray)):
        raise TypeError("Input must be a list, tuple, or NumPy array.")
    if len(data) == 0:
        raise ValueError("Input data cannot be empty.")
    try:
        array = np.asarray(data)
        if not np.issubdtype(array.dtype, np.number):
            raise ValueError("Input data must contain numeric values.")
        return float(np.mean(array))
    except Exception as e:
        raise ValueError(f"Error calculating mean: {e}")

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = calculate_mean(sample_data)
    print(result)