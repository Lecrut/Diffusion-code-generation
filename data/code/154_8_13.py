import numpy as np

def count_occurrences(data):
    if not isinstance(data, (list, np.ndarray)):
        raise ValueError("Input must be a list or a numpy array")
    
    unique, counts = np.unique(data, return_counts=True)
    return dict(zip(unique, counts))

if __name__ == '__main__':
    sample_data = [1, 2, 2, 3, 3, 3]
    try:
        result = count_occurrences(sample_data)
        print(result)
    except ValueError as e:
        print(e)