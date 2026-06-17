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
    elif isinstance(data_structure, list):
        for item in data_structure:
            if isinstance(item, tuple) and len(item) >= 2:
                try:
                    value = int(item[1])
                    unique_items.add(value)
                except (ValueError, TypeError):
                    continue
    return len(unique_items)
if __name__ == '__main__':
    sample_sparse_matrix = [
        ['0', '5'], ['0', '3'], ['0', '8'], 
        ['1', '2'], ['0', '9']
    ]
    sample_hash_map_data = {
        1: 'A', 2: 'B', 3: 'C', 4: 'D'
    }
    sparse_count = count_sparse_items(sample_sparse_matrix)
    hash_count = optimize_hash_map_count(sample_hash_map_data)
    print(f"Sparse Matrix Item Count: {sparse_count}")
    print(f"Hash Map Unique Value Count: {hash_count}")