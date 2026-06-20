class BooleanChecker:
    FALSE = False

    @staticmethod
    def are_both_false(a, b):
        return a == BooleanChecker.FALSE and b == BooleanChecker.FALSE

if __name__ == '__main__':
    checker = BooleanChecker()
    print(checker.are_both_false(False, False))
    print(checker.are_both_false(True, False))
    print(checker.are_both_false(False, True))
    print(checker.are_both_false(True, True))