class BooleanChecker:
    def check_both_false(self, a: bool, b: bool) -> bool:
        return not a and not b
if __name__ == '__main__':
    checker = BooleanChecker()
    a1 = False
    b1 = False
    result1 = checker.check_both_false(a1, b1)
    print(f"Test 1 (False, False): {result1}")
    a2 = True
    b2 = False
    result2 = checker.check_both_false(a2, b2)
    print(f"Test 2 (True, False): {result2}")
    a3 = True
    b3 = True
    result3 = checker.check_both_false(a3, b3)
    print(f"Test 3 (True, True): {result3}")
    a4 = False
    b4 = True
    result4 = checker.check_both_false(a4, b4)
    print(f"Test 4 (False, True): {result4}")