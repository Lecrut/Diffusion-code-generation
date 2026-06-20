class ConditionEvaluator:
    @staticmethod
    def both_true(a: bool, b: bool) -> bool:
        return a and b

if __name__ == '__main__':
    print(f"both_true(True, True): {ConditionEvaluator.both_true(True, True)}")
    print(f"both_true(True, False): {ConditionEvaluator.both_true(True, False)}")
    print(f"both_true(False, True): {ConditionEvaluator.both_true(False, True)}")
    print(f"both_true(False, False): {ConditionEvaluator.both_true(False, False)}")