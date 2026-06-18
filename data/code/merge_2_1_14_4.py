from typing import Any
class ConditionChecker:
    @staticmethod
    def evaluate_condition(condition_func: callable, *args) -> bool:
        try:
            return condition_func(*args)
        except Exception as e:
            raise TypeError(f"Error evaluating condition: {e}")
if __name__ == '__main__':
    def sample_check(value: int, threshold: float = 10) -> bool:
        return value > threshold
    checker = ConditionChecker()
    test_values = [5, 20, -3]
    thresholds = [10.0, 7.5, 25.0]
    results: list[bool] = []
    for value in test_values:
        threshold = thresholds[test_values.index(value) % len(thresholds)]
        is_greater = checker.evaluate_condition(sample_check, value, threshold)
        results.append(is_greater)
    print("Evaluation Results:", results)