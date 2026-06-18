from typing import Any
class PositiveValueEvaluator:
    def __init__(self, value: float) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a numeric type.")
        self._value = value
    def is_positive(self) -> bool:
        return self._value > 0
if __name__ == '__main__':
    evaluator = PositiveValueEvaluator(10)
    print(evaluator.is_positive())
    evaluator2 = PositiveValueEvaluator(-5)
    print(evaluator2.is_positive())
    try:
        evaluator3 = PositiveValueEvaluator("not a number")                             
    except TypeError as e:
        print(f"Error occurred: {e}")