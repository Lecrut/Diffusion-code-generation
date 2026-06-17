import sys
from collections import defaultdict
def count_sparse_items(matrix_data):
    if not isinstance(matrix_data, list) or len(matrix_data) == 0:
        return 0
    item_counts = defaultdict(int)
    for row in matrix_data:
        if not isinstance(row, (list, tuple)) or len(row) < 2:
            continue
        try:
            value = int(row[1])
            count = sum(1 for x in range(len(row)-1) if row[x] == '0') + 1
            item_counts[value] += count
        except (ValueError, IndexError):
            continue
    return len(item_counts)
def optimize_hash_map_count(data_structure):
    unique_items = set()
    if isinstance(data_structure, dict):
        for key in data_structure.keys():
            try:
                val = int(key)
                unique_items.add(val)
            except (ValueError, TypeError):
                pass
    elif hasattr(data_structure, '__iter__') and not isinstance(data_structure, str):
        for item in data_structure:
            if isinstance(item, dict):
                try:
                    val = int(list(item.keys())[0])
                    unique_items.add(val)
                except (ValueError, IndexError):
                    pass
    return len(unique_items)
if __name__ == '__main__':
    sparse_matrix = [
        ['A', 1], ['B', 2], ['C', 3],
        ['D', 4], ['E', 5]
    ]
    hash_map_data = {
        'x': 10, 'y': 20, 'z': 30,
        'a': 40, 'b': 50
    }
    result_sparse = count_sparse_items(sparse_matrix)
    result_hash = optimize_hash_map_count(hash_map_data)
    print(f"Sparse Matrix Count: {result_sparse}")
    print(f"Hash Map Count: {result_hash}")