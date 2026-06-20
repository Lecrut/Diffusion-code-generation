class BooleanEvaluator:
    @staticmethod
    def check_both_true(a: bool, b: bool) -> bool:
        return a and b

if __name__ == '__main__':
    print(BooleanEvaluator.check_both_true(True, True))
    print(BooleanEvaluator.check_both_true(False, True))
    print(BooleanEvaluator.check_both_true(True, False))
    print(BooleanEvaluator.check_both_true(False, False))