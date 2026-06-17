import time
from collections import defaultdict
def count_sparse_items(matrix_data):
    count_map = defaultdict(int)
    start_time = time.perf_counter()
    for item in matrix_data:
        if len(item) >= 3 and isinstance(item[2], (int, float)):
            value = item[2]
            count_map[value] += 1
    end_time = time.perf_counter()
    return dict(count_map), int((end_time - start_time) * 1_000_000)
if __name__ == '__main__':
    sample_data = [
        (0, 5, 1.2),
        (0, 8, 3.4),
        (1, 2, 7.9),
        (1, 6, 7.9),
        (2, 3, 2.1),
        (3, 5, 1.2),
        (4, 0, 8.8)
    ]
    counts, duration = count_sparse_items(sample_data)
    print(f"Counts: {counts}")
    print(f"Time taken ({duration:.6f} microseconds):")