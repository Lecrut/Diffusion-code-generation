import math
from typing import List, Tuple
def calculate_group_ranges(list_a: List[float], list_b: List[float]) -> List[Tuple[int, float]]:
    def safe_range(values: List[float]) -> float:
        if not values:
            return 0.0
        sorted_vals = sorted(values)
        max_val = -math.inf
        min_val = math.inf
        for val in sorted_vals:
            if val > max_val:
                max_val = val
            elif val < min_val:
                min_val = val
        return float(max_val - min_val)
    results = []
    n = min(len(list_a), len(list_b))
    if n == 0:
        return []
    ranges = []
    for i in range(n):
        pair_values = [list_a[i], list_b[i]]
        group_range = safe_range(pair_values)
        results.append((i, group_range))
    results.sort(key=lambda x: x[0])
    return results
if __name__ == '__main__':
    sample_list_a = [1.5e-4, 2.3e+6, -9.8e-7]
    sample_list_b = [1.0e-4, 2.0e+6, -1.0e-6]
    output_data = calculate_group_ranges(sample_list_a, sample_list_b)
    for index, range_val in output_data:
        print(f"Group {index}: Range = {range_val}")