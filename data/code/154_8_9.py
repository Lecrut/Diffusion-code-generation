import numpy as np

ITEM_COUNT_DICT = "item_count_dict"

def count_items(sequence):
    unique, counts = np.unique(sequence, return_counts=True)
    return dict(zip(unique, counts))

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50, 50, 50]
    result = count_items(sample_data)
    print(result)