import numpy as np

def validate_input(data):
    if not isinstance(data, (list, tuple)):
        raise ValueError("Input must be a list or tuple")

def count_occurrences(data):
    validate_input(data)
    unique, counts = np.unique(data, return_counts=True)
    return dict(zip(unique, counts))

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50, 50, 50]
    result = count_occurrences(sample_data)
    print(result)