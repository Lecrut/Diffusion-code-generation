class BooleanChecker:
    def __init__(self):
        self.false_value = False

    def check_both_false(self, a: bool, b: bool) -> bool:
        return a is self.false_value and b is self.false_value

if __name__ == '__main__':
    checker = BooleanChecker()
    print(checker.check_both_false(False, False))
    print(checker.check_both_false(False, True))
    print(checker.check_both_false(True, False))
    print(checker.check_both_false(True, True))
    print(checker.check_both_false(0, 0))
    print(checker.check_both_false(1, 0))