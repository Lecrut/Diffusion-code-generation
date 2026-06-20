class ConditionEvaluator:
    def evaluate_or(self, condition):
        return any(condition)

if __name__ == '__main__':
    evaluator = ConditionEvaluator()
    print(evaluator.evaluate_or((True, False)))
    print(evaluator.evaluate_or((False, True)))
    print(evaluator.evaluate_or((False, False)))
    print(evaluator.evaluate_or((None, True)))
    print(evaluator.evaluate_or((0, True)))