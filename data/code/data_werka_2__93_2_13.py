class BooleanChecker:
    TRUE_VALUE = True
    FALSE_VALUE = False

    def check_both_false(self, a: bool, b: bool) -> bool:
        if not isinstance(a, bool) or not isinstance(b, bool):
            raise ValueError("Inputs must be boolean types")
        return not bool(a) and not bool(b)

if __name__ == '__main__':
    checker = BooleanChecker()
    val_a = False
    val_b = False
    print(checker.check_both_false(val_a, val_b))
    val_c = True
    print(checker.check_both_false(val_a, val_c))
    val_d = False
    print(checker.check_both_false(val_c, val_d))
    val_e = True
    print(checker.check_both_false(val_e, val_e))