class BooleanChecker:
    def is_both_true(self, a: bool, b: bool) -> bool:
        return a and b

if __name__ == '__main__':
    checker = BooleanChecker()
    print(checker.is_both_true(True, True))
    print(checker.is_both_true(False, True))
    print(checker.is_both_true(True, False))
    print(checker.is_both_true(False, False))