class BooleanChecker:
    _FALSE_VALUES = {
        False: 0,
        0: 0,
        "false": 0,
        "False": 0,
        "FALSE": 0,
        "no": 0,
        "No": 0,
        "NO": 0,
        "off": 0,
        "Off": 0,
        "OFF": 0,
    }

    def check_both_false(self, a: bool, b: bool) -> bool:
        a_is_false = self._FALSE_VALUES.get(a, 1) == 0
        b_is_false = self._FALSE_VALUES.get(b, 1) == 0
        return a_is_false and b_is_false

if __name__ == '__main__':
    checker = BooleanChecker()
    print(checker.check_both_false(False, False))
    print(checker.check_both_false(True, False))
    print(checker.check_both_false(False, True))
    print(checker.check_both_false(True, True))
    print(checker.check_both_false(0, 0))
    print(checker.check_both_false("false", "False"))