class FlagValidator:
    @staticmethod
    def validate(flag1, flag2):
        return bool(flag1 and flag2)

if __name__ == '__main__':
    validator = FlagValidator()
    print(validator.validate(True, True))
    print(validator.validate(True, False))
    print(validator.validate(False, True))
    print(validator.validate(False, False))