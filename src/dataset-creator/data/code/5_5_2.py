import time
from typing import List, Tuple
class SortValidator:
    def validate(self, data: List[int]) -> bool:
        if not isinstance(data, list):
            return False
        if len(data) < 2:
            return False
        try:
            [int(x) for x in data]
        except (ValueError, TypeError):
            return False
        return True
class PerformanceEngine:
    def __init__(self):
        self.validator = SortValidator()
    def get_sorted_data(self, data: List[int]) -> Tuple[List[int], int]:
        start_time = time.perf_counter_ns()
        sorted_list = sorted(data)
        end_time = time.perf_counter_ns()
        return sorted_list, (end_time - start_time) / 1_000_000
def main():
    raw_data: List[int] = [64, 34, 25, 12, 22, 11, 90, 87, 45, 33]
    if not self.validator.validate(raw_data):
        raise ValueError("Input validation failed")
    original_list: List[int] = raw_data.copy()
    sorted_result, execution_time = get_sorted_data(original_list)
    print(f"Original list length: {len(original_list)}")
    print(f"Execution time (built-in sort): {execution_time:.6f} ms")
if __name__ == '__main__':
    engine = PerformanceEngine()
    raw_data: List[int] = [64, 34, 25, 12, 22, 11, 90, 87, 45, 33]
    validator = SortValidator()
    if not validator.validate(raw_data):
        raise ValueError("Input validation failed")
    original_list: List[int] = raw_data.copy()
    start_time = time.perf_counter_ns()
    sorted_list = sorted(original_list)
    end_time = time.perf_counter_ns()
    execution_time_ms = (end_time - start_time) / 1_000_000
    print(f"Original list length: {len(original_list)}")
    print(f"Execution time (built-in sort): {execution_time_ms:.6f} ms")