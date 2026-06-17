from typing import Any
class ValueEvaluator:
    def __init__(self, initial_value: float) -> None:
        self.value = initial_value
    def is_positive(self) -> bool:
        return self.value > 0
if __name__ == '__main__':
    evaluator = ValueEvaluator(10)
    print(evaluator.is_positive())
    evaluator2 = ValueEvaluator(-5)
    print(evaluator2.is_positive())