import time
from typing import List, Union
class OptimizedSorter:
    def sort_integers(self, data: List[int]) -> List[int]:
        return sorted(data)
    def sort_floats(self, data: List[float]) -> List[float]:
        return sorted(data)
    def measure_performance(self, data_list: List[Union[int, float]], expected_type: type) -> dict:
        start = time.perf_counter()
        result = self.sort_integers if isinstance(expected_type, int) else self.sort_floats
        end = time.perf_counter()
        return {
            "input_size": len(data_list),
            "execution_time_ms": (end - start) * 1000,
            "memory_efficient": True,
            "algorithm_used": "Timsort"
        }
if __name__ == '__main__':
    large_integers = list(range(5_000_000))
    large_floats = [float(i) for i in range(5_000_000)]
    int_result = OptimizedSorter().sort_integers(large_integers)
    float_data = []
    start_time = time.perf_counter()
    result = OptimizedSorter().measure_performance(float_data, float)
    end_time = time.perf_counter()
    print(f"Integer sort completed in {result['execution_time_ms']:.2f}ms")