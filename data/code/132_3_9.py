class LogicEvaluator:
    def evaluate(self, a, b):
        return bool(a or b)

if __name__ == '__main__':
    evaluator = LogicEvaluator()
    print(evaluator.evaluate(True, True))
    print(evaluator.evaluate(True, False))
    print(evaluator.evaluate(False, True))
    print(evaluator.evaluate(False, False))