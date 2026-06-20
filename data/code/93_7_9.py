class BoolChecker:
    def check_both_false(self, a, b):
        return not (a or b)

if __name__ == '__main__':
    checker = BoolChecker()
    print(checker.check_both_false(False, False))
    print(checker.check_both_false(True, False))
    print(checker.check_both_false(False, True))
    print(checker.check_both_false(True, True))