import numpy as np

def count_occurrences(data):
    unique_values, counts = np.unique(data, return_counts=True)
    return dict(zip(unique_values, counts))
if __name__ == '__main__':
    sample_data = [1, 2, 2, 3, 3, 3]
    result = count_occurrences(sample_data)
    print(result)