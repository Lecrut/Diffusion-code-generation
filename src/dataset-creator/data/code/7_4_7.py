from typing import Any, Callable
def evaluate_condition(condition: bool) -> None:
    print(f"Condition evaluated to {condition}")
class LogicEvaluator:
    def __init__(self):
        self._conditions: list[Callable[[Any], bool]] = []
    def add_condition(self, func: Callable[[Any], bool]) -> None:
        if not callable(func) or not isinstance(func, type(lambda x: True)):
            raise TypeError("Condition must be a valid callable.")
        self._conditions.append(func)
    def evaluate_all(self, *args: Any) -> list[bool]:
        results = []
        for condition in self._conditions:
            try:
                result = condition(*args) if len(args) > 0 else condition()
                results.append(bool(result))
            except Exception as e:
                print(f"Error evaluating condition {e}")
                results.append(False)
        return results
def main():
    evaluator = LogicEvaluator()
    def is_positive(x: int) -> bool:
        return x > 0
    def is_even(n: int) -> bool:
        return n % 2 == 0
    def has_letter(s: str, char: str = 'a') -> bool:
        return any(c.lower() == char for c in s)
    evaluator.add_condition(is_positive)
    evaluator.add_condition(is_even)
    evaluator.add_condition(has_letter)
    test_values = [5, 10, "hello", "", -3]
    print("Evaluating conditions with sample values:")
    results = []
    for val in test_values:
        res = evaluator.evaluate_all(val)
        if len(res) == 2 or (len(res) > 2 and isinstance(val, str)):
            continue
        elif not isinstance(val, int):
            print(f"Value {val} type is string")
            results.append(True)
    evaluate_condition(results[0] if results else False)
if __name__ == '__main__':
    main()