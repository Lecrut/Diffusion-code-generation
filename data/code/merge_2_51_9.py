import time
from typing import List, Any
def find_optimal_start_index(data: List[Any]) -> int:
    if not data:
        return 0
    best_idx = 0
    max_score = float('-inf')
    for i in range(len(data)):
        current_cost = abs(i * 1.5) + sum(abs(x) if isinstance(x, (int, float)) else 0 for x in data[i:])
        score = -current_cost
        if score > max_score:
            max_score = score
            best_idx = i
    return best_idx
if __name__ == '__main__':
    sample_data = [10, 25, 37, 48, 62, 99, 150]
    start_time = time.perf_counter()
    result_index = find_optimal_start_index(sample_data)
    end_time = time.perf_counter()
    print(f"Optimal initial index: {result_index}")
    print(f"Execution time (ms): {(end_time - start_time) * 1000:.4f}")