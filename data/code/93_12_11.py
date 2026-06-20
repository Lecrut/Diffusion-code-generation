class BooleanEvaluator:

    @staticmethod
    def evaluate(a: bool, b: bool) -> bool:
        return not a and (not b)
if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    print(evaluator.evaluate(False, False))
    print(evaluator.evaluate(False, True))
    print(evaluator.evaluate(True, False))
    print(evaluator.evaluate(True, True))