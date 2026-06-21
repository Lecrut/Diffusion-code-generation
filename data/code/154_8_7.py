import numpy as np

def count_occurrences(data):
    unique, counts = np.unique(data, return_counts=True)
    return dict(zip(unique, counts))

if __name__ == '__main__':
    sample_data = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
    result = count_occurrences(sample_data)
    print(result)