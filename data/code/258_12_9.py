import numpy as np

def average_pairs(data):
    if not data:
        return 0
    try:
        pairs = np.array(data)
        if pairs.ndim != 2 or pairs.shape[1] != 2:
            raise ValueError("Data must be a list of lists with exactly two elements each.")
        flattened = pairs.flatten()
        total_sum = np.sum(flattened)
        count = len(flattened)
        return total_sum / count
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0

if __name__ == '__main__':
    sample_data = [[1, 2], [3, 4], [5, 6]]
    result = average_pairs(sample_data)
    print(result)