class BooleanChecker:
    TRUE_VAL = 1
    FALSE_VAL = 0
    EXPECTED_TYPES = (bool,)

    def check_both_false(self, a: bool, b: bool) -> bool:
        if not isinstance(a, self.EXPECTED_TYPES) or not isinstance(b, self.EXPECTED_TYPES):
            raise ValueError("Inputs must be boolean types")
        
        is_a_false = (a == self.FALSE_VAL)
        is_b_false = (b == self.FALSE_VAL)
        
        return is_a_false and is_b_false

if __name__ == '__main__':
    checker = BooleanChecker()
    val1 = checker.check_both_false(False, False)
    val2 = checker.check_both_false(False, True)
    val3 = checker.check_both_false(True, False)
    val4 = checker.check_both_false(True, True)
    
    print(val1)
    print(val2)
    print(val3)
    print(val4)