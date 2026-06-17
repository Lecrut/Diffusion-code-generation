from typing import Union
class PositiveEvaluator:
    def __init__(self, value: Union[int, float]) -> None:
        self.value = value
    def is_positive(self) -> bool:
        return self.value > 0
if __name__ == '__main__':
    evaluator = PositiveEvaluator(10)
    print(evaluator.is_positive())
    evaluator2 = PositiveEvaluator(-5)
    print(evaluator2.is_positive())
    evaluator3 = PositiveEvaluator(0.0)
    print(evaluator3.is_positive())