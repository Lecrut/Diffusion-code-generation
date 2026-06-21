import numpy as np
SAMPLE_DATA = [10, 20, 30, 40, 50, 50, 50]

def count_occurrences(data):
    unique_items, counts = np.unique(data, return_counts=True)
    return dict(zip(unique_items, counts))
if __name__ == '__main__':
    result = count_occurrences(SAMPLE_DATA)
    print(result)