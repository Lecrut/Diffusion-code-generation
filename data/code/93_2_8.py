class BooleanChecker:
    FALSE = False

    @staticmethod
    def is_false(value: bool) -> bool:
        return value == BooleanChecker.FALSE

    def check_both_false(self, a: bool, b: bool) -> bool:
        return self.is_false(a) and self.is_false(b)

if __name__ == '__main__':
    checker = BooleanChecker()
    print(checker.check_both_false(False, False))
    print(checker.check_both_false(False, True))
    print(checker.check_both_false(True, False))
    print(checker.check_both_false(True, True))