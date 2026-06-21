import numpy as np

def count_items(sequence):
    unique, counts = np.unique(sequence, return_counts=True)
    return dict(zip(unique, counts))

if __name__ == '__main__':
    sample_data = [100, 200, 300, 400, 500, 500, 500]
    result = count_items(sample_data)
    print(result)