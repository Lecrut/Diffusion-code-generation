class BooleanEvaluator:
    def are_both_false(self, a: bool, b: bool) -> bool:
        return not a and not b

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    print(evaluator.are_both_false(False, False))
    print(evaluator.are_both_false(True, False))
    print(evaluator.are_both_false(False, True))
    print(evaluator.are_both_false(True, True))