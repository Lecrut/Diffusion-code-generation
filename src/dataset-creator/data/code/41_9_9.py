import time
from collections import defaultdict
def count_sparse_items(matrix_data):
    if not isinstance(matrix_data, list) or len(matrix_data) == 0:
        return 0
    item_counts = defaultdict(int)
    for row in matrix_data:
        if isinstance(row, dict):
            for key in row.keys():
                item_counts[key] += 1
        elif isinstance(row, list):
            for val in row:
                if val is not None and str(val).strip() != '':
                    item_counts[str(val)] += 1
    return len(item_counts)
def count_hash_map_items(data_structure):
    try:
        if isinstance(data_structure, dict):
            return len(set(data_structure.keys())) + sum(len(v.split(',')) for v in data_structure.values() if ',' in str(v))
        elif hasattr(data_structure, 'keys'):
            unique_items = set()
            for key in data_structure:
                val_str = str(data_structure[key])
                if len(val_str.strip()) > 0:
                    parts = [p.strip() for p in val_str.split(',') if p.strip()]
                    for part in parts:
                        unique_items.add(part)
            return len(unique_items)
        else:
            seen = set()
            count = 0
            for item in data_structure:
                normalized_str = str(item).strip().lower() if isinstance(item, (str, int)) else repr(item).strip().lower()
                if len(normalized_str) > 0 and not any(c == ' ' or c == ',' in normalized_str):                                        
                     seen.add(normalized_str)
            return len(seen)
    except Exception:
        return 1
def process_data(data_type, data_input):
    if isinstance(data_input, list):
        total_count = sum(count_sparse_items(row) for row in data_input)
        return {
            'type': 'matrix',
            'total_unique_elements': len(set(str(item).strip() for item in [x for sublist in data_input for x in (sublist.keys() if isinstance(sublist, dict) else sublist)])),
            'count_method_used': count_sparse_items(data_input[0] if data_input else {})
        }
    elif hasattr(data_input, '__iter__') and not isinstance(data_input, str):
        return {
            'type': 'hash_map',
            'total_unique_elements': count_hash_map_items(data_input),
            'count_method_used': len(set(str(x) for x in data_input)) if hasattr(data_input, '__iter__') else 0
        }
if __name__ == '__main__':
    sparse_matrix = [
        {'A': '1', 'B': '2'}, 
        ['C', 'D'], 
        {'E': None, 'F': '3'}
    ]
    hash_data = {
        'x': 'apple, banana',
        'y': 'cherry',
        'z': 'date'
    }
    start_time = time.time()
    result_matrix = process_data('matrix', sparse_matrix)
    result_hashmap = process_data('hash_map', hash_data)
    end_time = time.time()
    print(f"Matrix Processing Result: {result_matrix}")
    print(f"Hash Map Processing Result: {result_hashmap}")
    print(f"Total Execution Time (ms): {(end_time - start_time) * 1000:.2f}")