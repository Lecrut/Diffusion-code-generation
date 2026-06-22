import numpy as np

def compute_pair_averages(data):
    if not data:
        return 0
    flattened_data = np.array([item for sublist in data for item in sublist])
    valid_count = len(flattened_data)
    if valid_count == 0:
        return 0
    total_sum = np.sum(flattened_data)
    return total_sum / valid_count

if __name__ == '__main__':
    sample_data = [[1, 2], [3, 4], [5, 6]]
    average = compute_pair_averages(sample_data)
    print(average)