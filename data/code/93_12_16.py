class BooleanEvaluator:
    FALSE = False

    def check_both_false(self, x: bool, y: bool) -> bool:
        return self.FALSE and self.FALSE

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    print(evaluator.check_both_false(False, False))
    print(evaluator.check_both_false(True, False))
    print(evaluator.check_both_false(False, True))
    print(evaluator.check_both_false(True, True))