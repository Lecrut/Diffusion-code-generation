class BoolEvaluator:
    @staticmethod
    def are_both_false(a, b):
        return not a and not b

if __name__ == '__main__':
    evaluator = BoolEvaluator()
    print(evaluator.are_both_false(False, False))
    print(evaluator.are_both_false(True, False))
    print(evaluator.are_both_false(False, True))
    print(evaluator.are_both_false(True, True))