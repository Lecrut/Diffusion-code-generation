class BoolValidator:
    def validate_both_true(self, state1: bool, state2: bool) -> bool:
        return state1 and state2

if __name__ == '__main__':
    validator = BoolValidator()
    print(validator.validate_both_true(True, True))
    print(validator.validate_both_true(True, False))
    print(validator.validate_both_true(False, True))
    print(validator.validate_both_true(False, False))