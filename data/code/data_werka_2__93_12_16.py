class DualBooleanEvaluator:
    def __init__(self, first: bool, second: bool) -> None:
        self.first = first
        self.second = second

    def evaluate(self) -> bool:
        return not self.first and not self.second

if __name__ == '__main__':
    evaluator1 = DualBooleanEvaluator(False, False)
    print(evaluator1.evaluate())
    evaluator2 = DualBooleanEvaluator(False, True)
    print(evaluator2.evaluate())
    evaluator3 = DualBooleanEvaluator(True, False)
    print(evaluator3.evaluate())
    evaluator4 = DualBooleanEvaluator(True, True)
    print(evaluator4.evaluate())