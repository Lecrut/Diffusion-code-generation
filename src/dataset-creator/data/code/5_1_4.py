import timeit
from typing import List, Tuple
class AlgorithmPerformanceComparator:
    def __init__(self):
        self.results: dict[str, float] = {}
    def run_algorithm(self, algorithm_func: callable, iterations: int) -> float:
        try:
            timer = timeit.Timer(algorithm_func=algorithm_func, number=iterations)
            elapsed_time = timer.timeit()
            return elapsed_time / iterations
        except Exception as e:
            raise RuntimeError(f"Execution failed for algorithm function {e}") from None
    def compare_algorithms(self, algorithms: List[Tuple[str, callable]], iterations: int = 100) -> dict[str, float]:
        try:
            if not isinstance(algorithms, list):
                raise TypeError("Algorithms input must be a list of tuples containing name and function.")
            for i, (name, func) in enumerate(algorithms):
                if not callable(func):
                    raise ValueError(f"Function at index {i} is not callable: {func}")
                self.results[name] = self.run_algorithm(func, iterations)
        except Exception as e:
            raise RuntimeError("Comparison process failed") from None
        return self.results
def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
def naive_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return naive_fibonacci(n - 1) + naive_fibonacci(n - 2)
if __name__ == '__main__':
    comparator = AlgorithmPerformanceComparator()
    algorithms_list: List[Tuple[str, callable]] = [
        ("Iterative Fibonacci", fibonacci),
        ("Recursive Fibonacci (Naive)", naive_fibonacci)
    ]
    iterations_count: int = 100
    try:
        performance_metrics = comparator.compare_algorithms(algorithms_list, iterations_count)
        print("Performance Metrics:")
        for name, time_taken in performance_metrics.items():
            print(f"{name}: {time_taken:.6f} seconds per iteration")
    except Exception as error:
        print(f"Error occurred during comparison: {error}")