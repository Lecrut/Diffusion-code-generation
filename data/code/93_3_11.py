class FalseEvaluator:
    def evaluate(self, x, y):
        return not x and not y

if __name__ == '__main__':
    evaluator = FalseEvaluator()
    print(evaluator.evaluate(False, False))
    print(evaluator.evaluate(True, False))
    print(evaluator.evaluate(False, True))
    print(evaluator.evaluate(True, True))