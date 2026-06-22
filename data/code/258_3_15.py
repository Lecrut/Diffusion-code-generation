import numpy as np

def calculate_average_of_pairs(pairs):
    total_sum = 0
    count = 0
    for pair in pairs:
        if isinstance(pair, list) and len(pair) == 2:
            total_sum += sum(pair)
            count += 2
    if count == 0:
        return np.array([0])
    average = total_sum / count
    return np.array([average])

if __name__ == '__main__':
    sample_pairs = [
        [1, 5],
        [10, 20],
        [3, 7]
    ]
    result = calculate_average_of_pairs(sample_pairs)
    print(result)