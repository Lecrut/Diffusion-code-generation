class BooleanChecker:
    FALSE_VALUE = False

    @staticmethod
    def is_false(value):
        return value == BooleanChecker.FALSE_VALUE

    def are_both_false(self, a, b):
        return self.is_false(a) and self.is_false(b)

if __name__ == '__main__':
    checker = BooleanChecker()
    print(checker.are_both_false(False, False))
    print(checker.are_both_false(True, False))
    print(checker.are_both_false(False, True))
    print(checker.are_both_false(True, True))