class BooleanChecker:
    def is_both_true(self, a: bool, b: bool) -> bool:
        if not isinstance(a, bool) or not isinstance(b, bool):
            raise ValueError("Inputs must be boolean values")
        return a and b

if __name__ == '__main__':
    checker = BooleanChecker()
    print(checker.is_both_true(True, True))
    print(checker.is_both_true(False, False))
    try:
        print(checker.is_both_true(1, 0))
    except ValueError as e:
        print(e)