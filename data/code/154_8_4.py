import numpy as np

def count_occurrences(data):
    unique, counts = np.unique(data, return_counts=True)
    return dict(zip(unique, counts))

if __name__ == '__main__':
    sample_data = [1, 2, 2, 3, 3, 3]
    print(count_occurrences(sample_data))