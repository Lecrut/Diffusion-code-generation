class BooleanChecker:
    FALSE_CONSTANT = False

    def check_both_false(self, a: bool, b: bool) -> bool:
        if not isinstance(a, bool) or not isinstance(b, bool):
            raise ValueError("Inputs must be boolean types")
        
        is_a_false = (a == self.FALSE_CONSTANT)
        is_b_false = (b == self.FALSE_CONSTANT)
        
        return is_a_false and is_b_false

if __name__ == '__main__':
    checker = BooleanChecker()
    print(checker.check_both_false(False, False))
    print(checker.check_both_false(True, False))
    print(checker.check_both_false(False, True))
    print(checker.check_both_false(True, True))