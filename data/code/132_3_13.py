class LogicalEvaluator:
    def evaluate_or(self, a: bool, b: bool) -> bool:
        return bool(a or b)

if __name__ == '__main__':
    evaluator = LogicalEvaluator()
    print(evaluator.evaluate_or(True, True))
    print(evaluator.evaluate_or(True, False))
    print(evaluator.evaluate_or(False, True))
    print(evaluator.evaluate_or(False, False))