import numpy as np

def average_pairs(pairs):
    valid_pairs = [pair for pair in pairs if isinstance(pair, list) and len(pair) == 2]
    if not valid_pairs:
        return np.array([0])
    total_sum = sum(sum(pair) for pair in valid_pairs)
    count = len(valid_pairs) * 2
    average = total_sum / count
    return np.array([average])

if __name__ == '__main__':
    sample_pairs = [
        [1, 5],
        [10, 20],
        [3, 7]
    ]
    result = average_pairs(sample_pairs)
    print(result)