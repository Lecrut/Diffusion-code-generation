import numpy as np

def average_pairs(pairs):
    total_sum = 0
    pair_count = 0
    for pair in pairs:
        if isinstance(pair, list) and len(pair) == 2:
            total_sum += sum(pair)
            pair_count += 1
    if pair_count == 0:
        return np.array([0])
    else:
        average = total_sum / pair_count
        return np.array([average])

if __name__ == '__main__':
    sample_pairs = [
        [2, 4],
        [6, 8],
        [10, 12]
    ]
    result = average_pairs(sample_pairs)
    print(result)