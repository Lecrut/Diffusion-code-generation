import timeit
from typing import List, Tuple
class ComparisonEngine:
    def validate_input(self, data1: list, data2: list) -> bool:
        if not isinstance(data1, list) or not isinstance(data2, list):
            return False
        try:
            [int(x) for x in data1] + [int(y) for y in data2]
        except ValueError:
            return False
        return True
    def sort_builtin(self, data: List[int]) -> Tuple[List[int], float]:
        start = timeit.default_timer()
        sorted_data = sorted(data)
        elapsed = timeit.default_timer() - start
        return sorted_data, elapsed
    def compare_lists(self, list_a: List[int], list_b: List[int]) -> dict:
        if not self.validate_input(list_a, list_b):
            raise ValueError("Input validation failed")
        result_a, time_a = self.sort_builtin(list_a)
        result_b, time_b = self.sort_builtin(list_b)
        return {
            "list_a_sorted": result_a,
            "list_b_sorted": result_b,
            "time_list_a_ms": round(time_a * 1000, 4),
            "time_list_b_ms": round(time_b * 1000, 4)
        }
if __name__ == '__main__':
    sample_data_1 = [53, 29, -78, 62, 14]
    sample_data_2 = [-45, 102, 0, 33, -99]
    engine = ComparisonEngine()
    try:
        output = engine.compare_lists(sample_data_1, sample_data_2)
        print(output)
    except ValueError as e:
        print(f"Validation Error: {e}")