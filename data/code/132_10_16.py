class LogicEvaluator:

    def evaluate(self, a: bool, b: bool, c: bool) -> bool:
        return a and b or not c
if __name__ == '__main__':
    evaluator = LogicEvaluator()
    print(evaluator.evaluate(True, False, True))
    print(evaluator.evaluate(False, False, False))
    print(evaluator.evaluate(True, True, False))
    print(evaluator.evaluate(False, True, True))