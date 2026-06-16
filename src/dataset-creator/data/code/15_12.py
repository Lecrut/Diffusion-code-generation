import timeit
from typing import List, Tuple
def sort_numerical_data(data: List[float]) -> List[float]:
    return sorted(data)
if __name__ == '__main__':
    sample_data = [3.14, 2.718, -0.5, 99.9, 0.0] * 1000
    start_time = timeit.default_timer()
    result = sort_numerical_data(sample_data)
    end_time = timeit.default_timer()
    print(f"Sorted data: {result[:3]}...{result[-3:]}")
    print(f"Execution time (approx): {(end_time - start_time) * 10**6:.2f} microseconds")