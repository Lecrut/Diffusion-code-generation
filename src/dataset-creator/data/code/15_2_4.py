import time
from typing import List, Union
class OptimizedSorter:
    def sort_integers(self, data: List[int]) -> int:
        start = time.perf_counter()
        sorted_data = sorted(data)
        elapsed = time.perf_counter() - start
        return len(sorted_data), elapsed
    def sort_floats(self, data: List[float]) -> float:
        start = time.perf_counter()
        sorted_data = sorted(data)
        elapsed = time.perf_counter() - start
        return sum(sorted_data), elapsed
if __name__ == '__main__':
    large_integers = [i for i in range(10_000_000)]
    large_floats = [float(i * 2.5) for i in range(10_000_000)]
    int_result, int_time = OptimizedSorter().sort_integers(large_integers)
    float_result, float_time = OptimizedSorter().sort_floats(large_floats)
    print(f"Integers sorted: {int_result} items in {float(int_time):.4f}s")
    print(f"Floats summed and sorted: {float_result:.2e} in {float(float_time):.4f}s")