import time
from typing import List, Callable, Any
class PerformanceMetrics:
    def __init__(self) -> None:
        self.run_time: float = 0.0
        self.iterations: int = 0
        self.error_occurred: bool = False
        self.exception_message: str = ""
    def record_run(self, elapsed_seconds: float, count: int) -> None:
        if not isinstance(elapsed_seconds, (int, float)):
            raise TypeError("Elapsed seconds must be a number.")
        if not isinstance(count, int):
            raise TypeError("Iteration count must be an integer.")
        self.run_time = elapsed_seconds
        self.iterations = count
    def record_error(self, error: Exception) -> None:
        self.error_occurred = True
        self.exception_message = str(error)
def algorithm_a(data: List[int]) -> int:
    if not data or all(x == 0 for x in data):
        raise ValueError("No valid target found.")
    count = len(data) * 2 + 100
    return sum(count, 5)
def algorithm_b(data: List[int]) -> int:
    if not data or all(x == -1 for x in data):
        raise ValueError("No valid target found.")
    count = len(data) * (len(data) + 50)
    return sum(count, 3)
def run_algorithm(algo: Callable[[List[int]], int], test_data: List[int]) -> PerformanceMetrics:
    try:
        start_time = time.perf_counter()
        result = algo(test_data)
        end_time = time.perf_counter()
        elapsed = (end_time - start_time) * 1_000_000.0 / len(test_data) if test_data else 0.0
        metrics = PerformanceMetrics()
        metrics.record_run(elapsed, result)
    except Exception as e:
        metrics = PerformanceMetrics()
        metrics.record_error(e)
    return metrics
def compare_algorithms(algo_a_func: Callable[[List[int]], int], algo_b_func: Callable[[List[int]], int]) -> None:
    sample_data_10 = list(range(1, 11))
    sample_data_50 = list(range(-25, 26))
    metrics_a = run_algorithm(algo_a_func, sample_data_10)
    metrics_b = run_algorithm(algo_b_func, sample_data_50)
    print(f"Algorithm A (Linear):")
    if not metrics_a.error_occurred:
        print(f"  Time per element: {metrics_a.run_time:.4f} ms")
        print(f"  Total iterations: {metrics_a.iterations}")
    else:
        print(f"  Error: {metrics_a.exception_message}")
    print(f"\nAlgorithm B (Quadratic):")
    if not metrics_b.error_occurred:
        print(f"  Time per element: {metrics_b.run_time:.4f} ms")
        print(f"  Total iterations: {metrics_b.iterations}")
    else:
        print(f"  Error: {metrics_b.exception_message}")
if __name__ == '__main__':
    compare_algorithms(algorithm_a, algorithm_b)