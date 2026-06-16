from typing import List, Tuple
class AlgorithmPerformanceTracker:
    def __init__(self) -> None:
        self.results: dict[str, float] = {}
    def run_algorithm(self, algorithm_name: str, data_list: List[int]) -> float:
        try:
            if not isinstance(data_list, list):
                raise TypeError("Input must be a list.")
            n = len(data_list)
            simulated_cost = (n ** 2 + n * 10) / 1_000_000.0
            self.results[algorithm_name] = simulated_cost
            return simulated_cost
        except Exception as e:
            raise RuntimeError(f"Algorithm execution failed for {algorithm_name}: {e}")
def compare_algorithms(algorithm_a: str, algorithm_b: str) -> Tuple[float, float]:
    sample_data = [10, 25, 30, 45, 60]
    tracker = AlgorithmPerformanceTracker()
    try:
        metric_a = tracker.run_algorithm(algorithm_a, sample_data)
        metric_b = tracker.run_algorithm(algorithm_b, sample_data)
        return metric_a, metric_b
    except Exception as e:
        raise RuntimeError(f"Comparison failed due to error: {e}")
if __name__ == '__main__':
    try:
        result_a, result_b = compare_algorithms("Algorithm X", "Algorithm Y")
        print(f"{result_a=}")
        print(f"{result_b=}")
        if not (isinstance(result_a, float) and isinstance(result_b, float)):
            raise ValueError("Performance metrics must be numeric.")
    except Exception as e:
        error_message = str(e)
        print(error_message)