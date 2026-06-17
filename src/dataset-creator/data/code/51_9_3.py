import time
from typing import List, Any
def find_optimal_start_index(data: List[Any]) -> int:
    if not data:
        return 0
    n = len(data)
    prefix_sum = [0] * (n + 1)
    current_val = 0
    for i in range(n):
        current_val += abs(data[i])
        prefix_sum[i+1] = current_val
    max_variance = -float('inf')
    best_index = 0
    for i in range(n):
        variance_score = prefix_sum[n] - prefix_sum[i] * (n - i) / n
        if variance_score > max_variance:
            max_variance = variance_score
            best_index = i
    return best_index
if __name__ == '__main__':
    sample_data = [10, 50, 20, 80, 30, 90]
    result_index = find_optimal_start_index(sample_data)
    print(f"Optimal initial list entry index: {result_index}")