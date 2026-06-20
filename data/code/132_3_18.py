class LogicEvaluator:
    def evaluate_or(self, A, B):
        return bool(A or B)

if __name__ == '__main__':
    evaluator = LogicEvaluator()
    print(evaluator.evaluate_or(True, True))
    print(evaluator.evaluate_or(True, False))
    print(evaluator.evaluate_or(False, True))
    print(evaluator.evaluate_or(False, False))