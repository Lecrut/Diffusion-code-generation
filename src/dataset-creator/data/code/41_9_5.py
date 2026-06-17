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
            item_counts[value] += 1
        except (ValueError, IndexError):
            continue
    return len(item_counts)
def optimize_hash_map_count(data_structure):
    if not isinstance(data_structure, dict):
        data_structure = defaultdict(int)
    count = 0
    for key in data_structure:
        val = data_structure[key]
        if isinstance(val, int):
            count += 1
    return count
def main():
    sparse_matrix_data = [
        [0, 5], [0, 8], 
        [2, 3], [4, 7], 
        [6, 10], [9, 12]
    ]
    hash_map_data = {
        'apple': 5,
        'banana': 3,
        'cherry': 7,
        'date': 0
    }
    result1 = count_sparse_items(sparse_matrix_data)
    result2 = optimize_hash_map_count(hash_map_data)
    print(f"Sparse Matrix Unique Item Count: {result1}")
    print(f"Hash Map Total Entries Count: {result2}")
if __name__ == '__main__':
    main()