class BoolChecker:

    def both_false(self, A: bool, B: bool) -> bool:
        return not A and (not B)
if __name__ == '__main__':
    checker = BoolChecker()
    print(checker.both_false(False, False))
    print(checker.both_false(True, False))
    print(checker.both_false(False, True))
    print(checker.both_false(True, True))