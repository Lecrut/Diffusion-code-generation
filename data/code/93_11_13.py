class BooleanChecker:
    FALSE = False

    @staticmethod
    def are_both_false(a, b):
        return not a and not b

if __name__ == '__main__':
    checker = BooleanChecker()
    print(checker.are_both_false(BooleanChecker.FALSE, BooleanChecker.FALSE))
    print(checker.are_both_false(BooleanChecker.FALSE, True))
    print(checker.are_both_false(True, BooleanChecker.FALSE))
    print(checker.are_both_false(True, True))