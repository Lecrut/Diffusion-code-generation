class ConditionEvaluator:
    @staticmethod
    def is_both_true(a: bool, b: bool) -> bool:
        return a and b

if __name__ == '__main__':
    print(f"is_both_true(True, True): {ConditionEvaluator.is_both_true(True, True)}")
    print(f"is_both_true(True, False): {ConditionEvaluator.is_both_true(True, False)}")
    print(f"is_both_true(False, True): {ConditionEvaluator.is_both_true(False, True)}")
    print(f"is_both_true(False, False): {ConditionEvaluator.is_both_true(False, False)}")