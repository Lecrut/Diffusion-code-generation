class PositiveEvaluator:
    def __init__(self, initial_value):
        if not isinstance(initial_value, int):
            raise TypeError("initial_value must be an integer.")
        self._value = initial_value
    def is_positive(self) -> bool:
        return self._value > 0
if __name__ == '__main__':
    evaluator1 = PositiveEvaluator(5)
    print(f"Value {evaluator1._value} is positive: {evaluator1.is_positive()}")
    evaluator2 = PositiveEvaluator(-3)
    print(f"Value {evaluator2._value} is positive: {evaluator2.is_positive()}")
    evaluator3 = PositiveEvaluator(0)
    print(f"Value {evaluator3._value} is positive: {evaluator3.is_positive()}")