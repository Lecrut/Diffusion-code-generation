class BoolChecker:
    def are_both_true(self, val1, val2):
        return bool(val1) and bool(val2)

if __name__ == '__main__':
    checker = BoolChecker()
    print(checker.are_both_true(True, True))
    print(checker.are_both_true(False, True))
    print(checker.are_both_true(True, False))
    print(checker.are_both_true(False, False))