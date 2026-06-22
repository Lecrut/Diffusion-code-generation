import numpy as np

def average_pairs(data):
    if not data:
        return 0
    flattened = [item for sublist in data for item in sublist]
    array = np.array(flattened)
    return np.mean(array)

if __name__ == '__main__':
    sample_data = [[1, 2], [3, 4], [5, 6]]
    result = average_pairs(sample_data)
    print(result)