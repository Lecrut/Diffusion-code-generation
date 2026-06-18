import time
from collections import defaultdict
def count_sparse_matrix(items):
    item_counts = defaultdict(int)
    for row_items in items:
        for item in row_items:
            if isinstance(item, dict):
                key = tuple(sorted(item.items()))
            else:
                key = (item,)
            item_counts[key] += 1
    return list(item_counts.values())
def count_hash_map(items_list):
    counts = defaultdict(int)
    for item_group in items_list:
        if isinstance(item_group, dict):
            for key, value in item_group.items():
                counts[key] += 1
        elif isinstance(item_group, list):
            for val in item_group:
                counts[val] += 1
    return len(counts)
if __name__ == '__main__':
    sparse_data = [
        {'a': 1, 'b': 2},
        {'c': 3},
        {'d': 4}
    ]
    hash_map_data = [
        ['item_x', 'item_y'],
        ['item_z', 'item_x']
    ]
    start_time = time.time()
    result_sparse = count_sparse_matrix(sparse_data)
    result_hashmap = count_hash_map(hash_map_data)
    end_time = time.time()
    print(f"Sparse matrix unique item counts: {result_sparse}")
    print(f"Hash map total items counted: {result_hashmap}")