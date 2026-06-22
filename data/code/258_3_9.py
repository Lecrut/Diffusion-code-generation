import numpy as np

def average_pairs(pairs):
    total_sum = 0
    pair_count = 0
    for pair in pairs:
        if isinstance(pair, list) and len(pair) == 2:
            total_sum += sum(pair)
            pair_count += 1
    if pair_count == 0:
        return np.array([])
    else:
        return np.array([total_sum / pair_count])

if __name__ == '__main__':
    sample_pairs = [
        [1, 5],
        [10, 20],
        [3, 7]
    ]
    result = average_pairs(sample_pairs)
    print(result)