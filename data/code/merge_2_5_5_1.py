import timeit
from typing import List, Tuple
class ComparisonEngine:
    def validate_input(self, list_a: List[int], list_b: List[int]) -> bool:
        if not isinstance(list_a, list) or not isinstance(list_b, list):
            return False
        try:
            [int(x) for x in list_a] + [int(x) for x in list_b]
            return True
        except ValueError:
            return False
    def sort_builtin(self, data: List[int]) -> None:
        data.sort()
    def run_comparison(self, test_data_1: List[int], test_data_2: List[int]) -> Tuple[float, float]:
        if not self.validate_input(test_data_1, test_data_2):
            raise ValueError("Input validation failed")
        iterations = 5000
        time_a = timeit.timeit(lambda: self.sort_builtin(list(test_data_1)), number=iterations)
        time_b = timeit.timeit(lambda: self.sort_builtin(list(test_data_2)), number=iterations)
        return time_a, time_b
if __name__ == '__main__':
    engine = ComparisonEngine()
    sample_list_integers = [543, 987, 102, 654, 321]
    sample_list_strings = ["apple", "banana", "cherry"]
    try:
        int_times = engine.run_comparison(sample_list_integers.copy(), sample_list_integers.copy())
        print(f"Integer Sort Times (A/B): {int_times[0]:.6f} / {int_times[1]:.6f}")
        str_times = engine.run_comparison(sample_list_strings, sample_list_strings)
        print(f"String Sort Times (A/B): {str_times[0]:.6f} / {str_times[1]:.6f}")
    except ValueError as e:
        print(e)