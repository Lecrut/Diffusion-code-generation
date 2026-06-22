from typing import Tuple

class ConditionEvaluator:
    _ZERO: float = 0.0

    @staticmethod
    def _validate_positive(val: float) -> bool:
        return val > ConditionEvaluator._ZERO

    @staticmethod
    def _validate_order(first: float, second: float) -> bool:
        return second < first

    @staticmethod
    def _validate_sum(first: float, second: float, target: float) -> bool:
        return target == first + second

    def check_conditions(self, a: float, b: float, c: float) -> bool:
        first_valid = self._validate_positive(a)
        second_valid = self._validate_order(a, b)
        third_valid = self._validate_sum(a, b, c)
        return first_valid and second_valid and third_valid

if __name__ == '__main__':
    evaluator = ConditionEvaluator()
    result = evaluator.check_conditions(1.5, 0.5, 2.0)
    print(result)