class BooleanChecker:
    FALSE_VAL = False

    def check_both_false(self, a: bool, b: bool) -> bool:
        return a is self.FALSE_VAL and b is self.FALSE_VAL

if __name__ == '__main__':
    checker = BooleanChecker()
    print(checker.check_both_false(False, False))
    print(checker.check_both_false(False, True))
    print(checker.check_both_false(True, False))
    print(checker.check_both_false(True, True))