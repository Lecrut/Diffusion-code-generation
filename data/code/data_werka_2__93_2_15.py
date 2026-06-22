class BooleanChecker:
    def check_both_false(self, a: bool, b: bool) -> bool:
        if not isinstance(a, bool):
            raise ValueError(f"Expected bool for a, got {type(a).__name__}")
        if not isinstance(b, bool):
            raise ValueError(f"Expected bool for b, got {type(b).__name__}")
        return a is False and b is False

if __name__ == '__main__':
    checker = BooleanChecker()
    val1 = checker.check_both_false(False, False)
    val2 = checker.check_both_false(False, True)
    val3 = checker.check_both_false(True, False)
    val4 = checker.check_both_false(True, True)
    print(val1)
    print(val2)
    print(val3)
    print(val4)