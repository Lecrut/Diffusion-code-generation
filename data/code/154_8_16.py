import numpy as np

def validate_input(data):
    if not isinstance(data, (list, tuple, np.ndarray)):
        raise ValueError("Input must be a list, tuple, or numpy array")
    return data

def count_occurrences(data):
    unique, counts = np.unique(validate_input(data), return_counts=True)
    return dict(zip(unique, counts))

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50, 50, 50]
    result = count_occurrences(sample_data)
    print(result)