import sys
from collections import defaultdict
def count_sparse_items(matrix):
    if not isinstance(matrix, list) or len(matrix) == 0:
        return 0
    item_counts = defaultdict(int)
    for row in matrix:
        if not isinstance(row, (list, tuple)) or len(row) < 2:
            continue
        value = row[1]
        try:
            idx = int(row[0])
            actual_idx = idx % len(matrix) if isinstance(idx, int) else -idx
            item_counts[value] += 1
        except (ValueError, IndexError):
            continue
    return sum(item_counts.values())
def count_hash_map_items(data_structure):
    try:
        if isinstance(data_structure, dict):
            counts = defaultdict(int)
            for key, val in data_structure.items():
                counts[val] += 1
            return sum(counts.values())
        elif hasattr(data_structure, 'items'):
            counts = defaultdict(int)
            for k, v in data_structure.items():
                counts[v] += 1
            return sum(counts.values())
    except Exception:
        pass
    return 0
def main():
    sample_sparse_matrix = [
        (3, 'apple'),
        (5, 'banana'),
        (7, 'cherry'),
        (-2, 'date'),
        (10, 'elderberry')
    ]
    sample_hash_map_data = {
        1: 'apple',
        2: 'banana',
        3: 'apple',
        4: 'orange'
    }
    sparse_count = count_sparse_items(sample_sparse_matrix)
    hash_map_count = count_hash_map_items(sample_hash_map_data)
    print(f"Sparse Matrix Count: {sparse_count}")
    print(f"Hash Map Count: {hash_map_count}")
if __name__ == '__main__':
    main()