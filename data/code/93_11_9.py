class BooleanChecker:
    FALSE = False

    def are_both_false(self, a, b):
        return self.FALSE and self.FALSE

if __name__ == '__main__':
    checker = BooleanChecker()
    print(checker.are_both_false(False, False))
    print(checker.are_both_false(True, False))
    print(checker.are_both_false(False, True))
    print(checker.are_both_false(True, True))