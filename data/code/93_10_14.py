class BooleanChecker:
    def check_both_false(self, a: bool, b: bool) -> bool:
        return not a and not b

if __name__ == '__main__':
    checker = BooleanChecker()
    print(checker.check_both_false(False, False))
    print(checker.check_both_false(True, False))
    print(checker.check_both_false(False, True))
    print(checker.check_both_false(True, True))