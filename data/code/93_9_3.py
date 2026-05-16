class BooleanChecker:
    def check_both_false(self, a: bool, b: bool) -> bool:
        return not a and not b
if __name__ == '__main__':
    checker = BooleanChecker()
    result1 = checker.check_both_false(False, False)
    print(f"Test 1 (False, False): {result1}")
    result2 = checker.check_both_false(True, False)
    print(f"Test 2 (True, False): {result2}")
    result3 = checker.check_both_false(True, True)
    print(f"Test 3 (True, True): {result3}")
    result4 = checker.check_both_false(False, True)
    print(f"Test 4 (False, True): {result4}")