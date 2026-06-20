class BoolChecker:
    def both_false(self, x, y):
        return not x and not y

if __name__ == '__main__':
    checker = BoolChecker()
    print(checker.both_false(False, False))
    print(checker.both_false(True, False))
    print(checker.both_false(False, True))
    print(checker.both_false(True, True))