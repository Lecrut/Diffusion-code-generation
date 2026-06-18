import timeit
from typing import List, Tuple
def validate_input(data: List[int]) -> bool:
    return all(isinstance(x, int) for x in data) and len(data) > 0
class ComparisonEngine:
    def __init__(self):
        self.results = []
    def run_builtin_sort(self, data: List[int], iterations: int = 10) -> float:
        if not validate_input(data):
            raise ValueError("Input must be a non-empty list of integers.")
        setup_code = f"import timeit; d={data}"
        stmt = "timeit.timeit(stmt='d.sort()', setup=setup_code, number=iterations)"
        elapsed = timeit.default_timer()
        for _ in range(iterations):
            data_copy = list(data)
            data_copy.sort()
        total_time = timeit.default_timer() - elapsed
        return total_time / iterations
    def run_quicksort(self, data: List[int], iterations: int = 10) -> float:
        if not validate_input(data):
            raise ValueError("Input must be a non-empty list of integers.")
        setup_code = f"import timeit; d={data}"
        elapsed = timeit.default_timer()
        for _ in range(iterations):
            data_copy = list(data)
            self._quicksort_recursive(data_copy, 0, len(data_copy) - 1)
        total_time = timeit.default_timer() - elapsed
        return total_time / iterations
    def _quicksort_recursive(self, arr: List[int], low: int, high: int):
        if low < high:
            pi = self._partition(arr, low, high)
            self._quicksort_recursive(arr, low, pi - 1)
            self._quicksort_recursive(arr, pi + 1, high)
    def _partition(self, arr: List[int], low: int, high: int) -> int:
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
if __name__ == '__main__':
    sample_data: List[int] = [64, 34, 25, 12, 22, 11, 90, 88, 76, 55, 44, 33, 22, 11, 10]
    engine = ComparisonEngine()
    builtin_time: float = engine.run_builtin_sort(sample_data)
    custom_time: float = engine.run_quicksort(sample_data)
    print(f"Builtin Sort Time (avg): {builtin_time:.6f}s")
    print(f"Custom Quicksort Time (avg): {custom_time:.6f}s")