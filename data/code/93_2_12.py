class BooleanChecker:
    _FALSE_MAP = {
        False: 0,
        True: 1,
    }

    def check_both_false(self, a: bool, b: bool) -> bool:
        val_a = self._FALSE_MAP.get(a)
        val_b = self._FALSE_MAP.get(b)
        if val_a is None or val_b is None:
            raise ValueError("Inputs must be boolean")
        return val_a == 0 and val_b == 0

if __name__ == '__main__':
    checker = BooleanChecker()
    print(checker.check_both_false(False, False))
    print(checker.check_both_false(False, True))
    print(checker.check_both_false(True, False))
    print(checker.check_both_false(True, True))