class BooleanChecker:
    _FALSE_VALUE = False

    def check_both_false(self, a: bool, b: bool) -> bool:
        if not isinstance(a, bool) or not isinstance(b, bool):
            raise ValueError("Inputs must be boolean types")
        return self._validate_false(a) and self._validate_false(b)

    def _validate_false(self, value: bool) -> bool:
        return value == self._FALSE_VALUE

if __name__ == '__main__':
    checker = BooleanChecker()
    print(checker.check_both_false(False, False))
    print(checker.check_both_false(False, True))
    print(checker.check_both_false(True, False))
    print(checker.check_both_false(True, True))