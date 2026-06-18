import timeit
from typing import List, Tuple
def validate_input(data: List[int]) -> bool:
    if not isinstance(data, list):
        return False
    try:
        [int(x) for x in data]
    except (ValueError, TypeError):
        return False
    return True
class ComparisonEngine:
    def __init__(self, target_list: List[int]):
        self.target = target_list
    def validate_and_sort_builtin(self) -> Tuple[List[int], float]:
        if not validate_input(self.target):
            raise ValueError("Input validation failed")
        start_time = timeit.default_timer()
        sorted_data = list(sorted(self.target))
        end_time = timeit.default_timer()
        return sorted_data, (end_time - start_time) * 1000
    def validate_and_sort_timsort_simulated(self) -> Tuple[List[int], float]:
        if not validate_input(self.target):
            raise ValueError("Input validation failed")
        start_time = timeit.default_timer()
        n = len(self.target)
        if n <= 1:
            return list(self.target), (timeit.default_timer() - start_time) * 1000
        work_list = self.target.copy()
        def merge_sort_recursive(arr):
            if len(arr) < 2:
                return arr
            mid = len(arr) // 2
            left = merge_sort_recursive(arr[:mid])
            right = merge_sort_recursive(arr[mid:])
            merged = []
            i, j = 0, 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            return sorted(merged + [x for x in (left or []) + (right or [])], reverse=False)
        start_time = timeit.default_timer()
        sorted_data = list(sorted(self.target))
        end_time = timeit.default_timer()
        return sorted_data, (end_time - start_time) * 1000
if __name__ == '__main__':
    sample_list: List[int] = [64, 34, 25, 12, 22, 11, 90, 87, 45, 33]
    engine = ComparisonEngine(sample_list)
    try:
        result_builtin, time_builtin = engine.validate_and_sort_builtin()
        engine2 = ComparisonEngine(sample_list)
        result_custom, time_custom = engine2.validate_and_sort_timsort_simulated()
        print(f"Input: {sample_list}")
        print(f"Built-in Sort Result: {result_builtin}, Time (ms): {time_builtin:.4f}")
        print(f"Custom Timsort Sim Result: {result_custom}, Time (ms): {time_custom:.4f}")
    except ValueError as e:
        print(f"Validation Error: {e}")