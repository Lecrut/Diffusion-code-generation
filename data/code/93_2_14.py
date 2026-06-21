class BooleanChecker:
    TRUE_VAL = 1
    FALSE_VAL = 0

    def check_both_false(self, a: bool, b: bool) -> bool:
        is_a_false = (a is False) or (a == self.FALSE_VAL)
        is_b_false = (b is False) or (b == self.FALSE_VAL)
        return is_a_false and is_b_false

if __name__ == '__main__':
    checker = BooleanChecker()
    r1 = checker.check_both_false(False, False)
    r2 = checker.check_both_false(False, True)
    r3 = checker.check_both_false(True, False)
    r4 = checker.check_both_false(True, True)
    r5 = checker.check_both_false(0, 0)
    print(r1, r2, r3, r4, r5)