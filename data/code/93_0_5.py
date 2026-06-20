class BooleanChecker:
    def both_false(self, a: bool, b: bool) -> bool:
        return not a and not b

if __name__ == '__main__':
    checker = BooleanChecker()
    print(checker.both_false(False, False))
    print(checker.both_false(True, False))
    print(checker.both_false(False, True))
    print(checker.both_false(True, True))