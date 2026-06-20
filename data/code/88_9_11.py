class BooleanChecker:

    def is_both_true(self, a: bool, b: bool) -> bool:
        return a and b
if __name__ == '__main__':
    checker = BooleanChecker()
    result1 = checker.is_both_true(True, True)
    print(result1)
    result2 = checker.is_both_true(False, True)
    print(result2)
    result3 = checker.is_both_true(True, False)
    print(result3)
    result4 = checker.is_both_true(False, False)
    print(result4)