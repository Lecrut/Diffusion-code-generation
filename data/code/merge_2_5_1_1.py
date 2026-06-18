from typing import List, Tuple, Callable, Any
class AlgorithmPerformanceTracker:
    def __init__(self) -> None:
        self.results: dict[str, float] = {}
    def run_algorithm(self, algorithm_name: str, data_list: List[Any], operation: Callable[[List[Any]], Any]) -> float:
        try:
            import time
            start_time = time.perf_counter()
            if not isinstance(data_list, list):
                raise TypeError(f"Expected 'list' type for input data, got {type(data_list).__name__}")
            result = operation(data_list)
            end_time = time.perf_counter()
            execution_time = end_time - start_time
            self.results[algorithm_name] = execution_time
            return execution_time
        except Exception as e:
            raise RuntimeError(f"Algorithm '{algorithm_name}' failed with error: {str(e)}")
def quick_sort(arr: List[int]) -> int:
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    sorted_list = quick_sort(left) + middle + quick_sort(right)
    return sorted_list
def bubble_sort(arr: List[int]) -> int:
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
def fibonacci(n: int) -> List[int]:
    seq = []
    a, b = 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq
def main() -> None:
    tracker = AlgorithmPerformanceTracker()
    sample_data_integers = list(range(100))
    sample_fibonacci_terms = 50
    sort_operations = {
        "Quick Sort": quick_sort,
        "Bubble Sort": bubble_sort
    }
    fib_operations = {
        "Fibonacci Generator (n=50)": lambda: fibonacci(sample_fibonacci_terms)
    }
    for name in sort_operations.keys():
        try:
            time_taken = tracker.run_algorithm(name, sample_data_integers.copy(), sort_operations[name])
            print(f"Algorithm '{name}' executed successfully. Time taken: {time_taken:.6f} seconds")
            if not isinstance(time_taken, (int, float)):
                raise TypeError("Execution time must be numeric.")
        except Exception as e:
            error_msg = f"{e}"
            print(f"Error during execution of '{name}': {error_msg}")
    try:
        fib_name = "Fibonacci Generator (n=50)"
        time_taken = tracker.run_algorithm(fib_name, [], lambda x: fibonacci(sample_fibonacci_terms))
        if not isinstance(time_taken, (int, float)):
            raise TypeError("Execution time must be numeric.")
    except Exception as e:
        error_msg = f"{e}"
        print(f"Error during execution of '{fib_name}': {error_msg}")
    if tracker.results:
        print("\n--- Performance Summary ---")
        for algo, time in sorted(tracker.results.items()):
            print(f"{algo}: {time:.6f}s")
if __name__ == '__main__':
    main()