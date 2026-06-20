class ConditionEvaluator:
    @staticmethod
    def are_strictly_true(a, b):
        return bool(a) and bool(b)

if __name__ == '__main__':
    evaluator = ConditionEvaluator()
    print(evaluator.are_strictly_true(True, True))
    print(evaluator.are_strictly_true(False, True))
    print(evaluator.are_strictly_true(True, False))
    print(evaluator.are_strictly_true(False, False))