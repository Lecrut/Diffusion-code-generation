class BooleanChecker:
    FALSE_CONSTANT = False

    @staticmethod
    def both_false(a: bool, b: bool) -> bool:
        return a == BooleanChecker.FALSE_CONSTANT and b == BooleanChecker.FALSE_CONSTANT

if __name__ == '__main__':
    checker = BooleanChecker()
    print(checker.both_false(False, False))
    print(checker.both_false(True, False))
    print(checker.both_false(False, True))
    print(checker.both_false(True, True))