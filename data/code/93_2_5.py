class BooleanChecker:
    FALSE_VALUE = False

    def check_both_false(self, a: bool, b: bool) -> bool:
        if not isinstance(a, bool) or not isinstance(b, bool):
            raise ValueError("Inputs must be boolean values")
        return a is self.FALSE_VALUE and b is self.FALSE_VALUE

if __name__ == '__main__':
    checker = BooleanChecker()
    result1 = checker.check_both_false(False, False)
    result2 = checker.check_both_false(False, True)
    result3 = checker.check_both_false(True, False)
    result4 = checker.check_both_false(True, True)
    print(result1)
    print(result2)
    print(result3)
    print(result4)