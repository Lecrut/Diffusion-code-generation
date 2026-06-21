import numpy as np

def validate_input(data):
    if not isinstance(data, np.ndarray) or data.size == 0:
        raise ValueError("Input must be a non-empty numpy array")

def find_min_max(data):
    validate_input(data)
    return np.min(data), np.max(data)

if __name__ == '__main__':
    sample_array = np.array([15, 3, 8, 22, 1, 40])
    minimum_val, maximum_val = find_min_max(sample_array)
    print(f"Array: {sample_array}")
    print(f"Minimum value: {minimum_val}")
    print(f"Maximum value: {maximum_val}")