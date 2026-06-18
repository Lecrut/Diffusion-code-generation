import time
from typing import List
def find_optimal_start_index(data: List[int]) -> int:
    if not data:
        return 0
    max_sum = float('-inf')
    current_sum = 0
    best_idx = 0
    for i, val in enumerate(data):
        current_sum += val
        if current_sum > max_sum:
            max_sum = current_sum
            best_idx = i
    return best_idx
if __name__ == '__main__':
    sample_data = [3, -1, 4, -2, 5, -6]
    start_time = time.perf_counter()
    result_index = find_optimal_start_index(sample_data)
    end_time = time.perf_counter()
    print(f"Optimal starting index: {result_index}")