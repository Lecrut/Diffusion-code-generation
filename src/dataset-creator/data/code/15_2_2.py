import time
from typing import List, Union
class OptimizedSorter:
    def sort_integers(self, data: List[int]) -> List[int]:
        return sorted(data)
    def sort_floats(self, data: List[float]) -> List[float]:
        return sorted(data)
    def benchmark_sort(self, data_type: str = 'int', size: int = 10_000_000) -> dict:
        if not isinstance(size, (int, float)) or size <= 0:
            raise ValueError("Size must be a positive number.")
        start_time = time.perf_counter()
        if data_type == 'int':
            sample_data = [random.randint(1, 2**31) for _ in range(size)]
        elif data_type == 'float':
            sample_data = [random.uniform(-1e6, 1e6) for _ in range(size)]
        sorted_data = self.sort_integers if data_type == 'int' else self.sort_floats(sample_data)
        end_time = time.perf_counter()
        return {
            "size": size,
            "data_type": data_type,
            "execution_time_seconds": round(end_time - start_time, 4),
            "memory_estimate_bytes": size * (8 if data_type == 'int' else 16)
        }
if __name__ == '__main__':
    import random
    sorter = OptimizedSorter()
    small_ints = [5, -2, 8.0, 3] 
    small_floats = [-1.5, 4.7, 0.0, 9.9]
    print("Sorting Small Integers:", sorter.sort_integers(small_ints))
    print("Sorting Small Floats:", sorter.sort_floats(small_floats))
    result = sorter.benchmark_sort(data_type='int', size=10_000)
    print(f"Performance Metrics for {result['size']} integers: {result}")