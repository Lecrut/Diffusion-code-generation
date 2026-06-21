class BooleanChecker:
    _FALSE_VALUES = (False, 0, None, "")

    def check_both_false(self, a: bool, b: bool) -> bool:
        if not isinstance(a, bool) or not isinstance(b, bool):
            raise ValueError("Inputs must be boolean types")
        return a is False and b is False

if __name__ == '__main__':
    checker = BooleanChecker()
    val1 = checker.check_both_false(False, False)
    val2 = checker.check_both_false(True, False)
    val3 = checker.check_both_false(False, True)
    val4 = checker.check_both_false(True, True)
    print(val1)
    print(val2)
    print(val3)
    print(val4)