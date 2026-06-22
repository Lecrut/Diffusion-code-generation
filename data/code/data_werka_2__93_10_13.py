class BooleanChecker:
    TRUE_VAL = 1
    FALSE_VAL = 0

    def are_both_false(self, val1, val2):
        bool1 = 1 if val1 else 0
        bool2 = 1 if val2 else 0
        return bool1 == self.FALSE_VAL and bool2 == self.FALSE_VAL

if __name__ == '__main__':
    checker = BooleanChecker()
    print(checker.are_both_false(False, False))
    print(checker.are_both_false(True, False))
    print(checker.are_both_false(False, True))
    print(checker.are_both_false(True, True))