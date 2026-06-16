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
    large_integers = [i for i in range(10_000)] + list(range(-500, 600))
    large_floats = [float(i) * (1.234 if i % 2 else -987.654) for i in range(10_000)]
    int_count, int_time = OptimizedSorter().sort_integers(large_integers)
    float_sum, float_time = OptimizedSorter().sort_floats(large_floats)
    print(f"Integers sorted: {int_count} items in {float(int_time):.6f}s")
    print(f"Floats summed after sort: {float_sum:.2f}")