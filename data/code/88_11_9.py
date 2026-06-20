class FlagValidator:
    def validate(self, flag1: bool, flag2: bool) -> bool:
        if not flag1 or not flag2:
            raise ValueError('At least one flag is false')
        return True

if __name__ == '__main__':
    validator = FlagValidator()
    print(validator.validate(True, True))
    print(validator.validate(True, False))
    print(validator.validate(False, True))