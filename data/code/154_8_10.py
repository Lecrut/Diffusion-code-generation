import numpy as np

def count_occurrences(data):
    if not isinstance(data, (list, tuple, np.ndarray)):
        raise ValueError("Input must be a list, tuple, or numpy array")
    
    unique, counts = np.unique(data, return_counts=True)
    return dict(zip(unique, counts))

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50, 50, 50]
    try:
        result = count_occurrences(sample_data)
        print(result)
    except ValueError as e:
        print(e)