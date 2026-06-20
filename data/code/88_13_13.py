class BooleanEvaluator:
    @staticmethod
    def are_strictly_true(var1, var2):
        return bool(var1) and bool(var2)

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    print(evaluator.are_strictly_true(True, True))
    print(evaluator.are_strictly_true(False, True))
    print(evaluator.are_strictly_true(True, False))
    print(evaluator.are_strictly_true(False, False))