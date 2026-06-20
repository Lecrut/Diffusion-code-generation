class BooleanValidator:
    def validate_both_true(self, flag1: bool, flag2: bool) -> bool:
        return flag1 and flag2

if __name__ == '__main__':
    validator = BooleanValidator()
    result1 = validator.validate_both_true(True, True)
    print(f"validate_both_true(True, True): {result1}")
    result2 = validator.validate_both_true(True, False)
    print(f"validate_both_true(True, False): {result2}")
    result3 = validator.validate_both_true(False, True)
    print(f"validate_both_true(False, True): {result3}")
    result4 = validator.validate_both_true(False, False)
    print(f"validate_both_true(False, False): {result4}")