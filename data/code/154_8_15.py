import numpy as np

def count_occurrences(data):
    unique, counts = np.unique(data, return_counts=True)
    return dict(zip(unique, counts))

if __name__ == '__main__':
    sample_data = [1, 2, 3, 3, 4, 5, 5, 5]
    occurrences = count_occurrences(sample_data)
    print(occurrences)