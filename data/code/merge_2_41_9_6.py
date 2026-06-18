import sys
from collections import defaultdict
def count_sparse_items(matrix_data):
    if not isinstance(matrix_data, list) or len(matrix_data) == 0:
        return 0
    item_counts = defaultdict(int)
    for row in matrix_data:
        if not isinstance(row, (list, tuple)):
            continue
        for value in row:
            try:
                hash(value)
                item_counts[value] += 1
            except TypeError:
                pass
    return len(item_counts)
def count_hash_map_items(data):
    if not isinstance(data, dict):
        return 0
    try:
        return len(set(data.keys()))
    except Exception:
        return 0
if __name__ == '__main__':
    sparse_matrix = [
        [1, 2],
        [3, None],
        [],
        [4]
    ]
    hash_map_data = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4
    }
    sparse_count = count_sparse_items(sparse_matrix)
    map_count = count_hash_map_items(hash_map_data)
    print(f"Sparse Matrix Unique Items: {sparse_count}")
    print(f"Hash Map Keys Count: {map_count}")