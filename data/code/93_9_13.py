class BooleanEvaluator:
    @staticmethod
    def is_both_false(a: bool, b: bool) -> bool:
        return not a and not b

if __name__ == '__main__':
    result1 = BooleanEvaluator.is_both_false(False, False)
    print(f"Test 1 (False, False): {result1}")
    result2 = BooleanEvaluator.is_both_false(True, False)
    print(f"Test 2 (True, False): {result2}")
    result3 = BooleanEvaluator.is_both_false(True, True)
    print(f"Test 3 (True, True): {result3}")
    result4 = BooleanEvaluator.is_both_false(False, True)
    print(f"Test 4 (False, True): {result4}")