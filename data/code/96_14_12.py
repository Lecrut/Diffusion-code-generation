class BooleanEvaluator:

    def evaluate(self, a: bool, b: bool) -> bool:
        c = not b or a
        return a and b or (not a and c)
if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    print(evaluator.evaluate(True, False))
    print(evaluator.evaluate(False, True))
    print(evaluator.evaluate(True, True))
    print(evaluator.evaluate(False, False))