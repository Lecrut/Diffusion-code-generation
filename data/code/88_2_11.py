class BooleanChecker:
    @staticmethod
    def are_both_true(val1, val2):
        return bool(val1) and bool(val2)

if __name__ == '__main__':
    checker = BooleanChecker()
    print(checker.are_both_true(True, True))
    print(checker.are_both_true(False, True))
    print(checker.are_both_true(True, False))
    print(checker.are_both_true(False, False))