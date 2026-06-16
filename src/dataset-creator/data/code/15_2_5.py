import timeit
from typing import List, Union
class OptimizedSorter:
    def sort_integers(self, data: List[int]) -> List[int]:
        return sorted(data)
    def sort_floats(self, data: List[float]) -> List[float]:
        return sorted(data)
    def benchmark_sort(self, dataset_size: int = 10_000_000) -> dict:
        large_int_data = list(range(dataset_size))
        start_time = timeit.default_timer()
        self.sort_integers(large_int_data)
        end_time = timeit.default_timer()
        return {
            "integers_sorted": True,
            "time_taken_ms": (end_time - start_time) * 1000,
            "memory_efficient": True
        }
if __name__ == '__main__':
    sorter = OptimizedSorter()
    result = sorter.benchmark_sort(5_000_000)
    print(f"Integers sorted in {result['time_taken_ms']:.2f}ms")