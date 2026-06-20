class BoolChecker:

    def are_both_false(self, a, b):
        return not a and (not b)
if __name__ == '__main__':
    checker = BoolChecker()
    print(checker.are_both_false(False, False))
    print(checker.are_both_false(True, False))
    print(checker.are_both_false(False, True))
    print(checker.are_both_false(True, True))