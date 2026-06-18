from typing import Union
class PositiveEvaluator:
    def __init__(self, value: Union[int, float]) -> None:
        self.value = value
    def is_positive(self) -> bool:
        return self.value > 0
if __name__ == '__main__':
    evaluator = PositiveEvaluator(10)
    print(evaluator.is_positive())