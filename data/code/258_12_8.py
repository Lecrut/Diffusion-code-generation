import numpy as np

def average_pairs(data):
    if not data:
        return 0
    pairs = np.array(data)
    try:
        total_sum = np.sum(pairs, axis=1)
        count = len(pairs)
        overall_average = total_sum / 2
        return overall_average.mean()
    except (ValueError, TypeError):
        return 0

if __name__ == '__main__':
    sample_data = [[1, 2], [3, 4], [5, 6]]
    print(average_pairs(sample_data))