from typing import Any
class ValueEvaluator:
    def __init__(self, initial_value: float) -> None:
        try:
            self._value: float = float(initial_value)
        except (ValueError, TypeError):
            raise TypeError("Initial value must be convertible to a float.")
    def is_positive(self) -> bool:
        return self._value > 0
if __name__ == '__main__':
    sample_values: list[float] = [1.5, -4.2, 0, 1e-6, float('-inf')]
    for val in sample_values:
        evaluator = ValueEvaluator(val)
        result = "Positive" if evaluator.is_positive() else "Non-positive"
        print(f"{val}: {result}")