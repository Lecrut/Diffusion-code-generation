class FlagValidator:
    def validate(self, flag1: bool, flag2: bool) -> bool:
        if not (flag1 and flag2):
            raise ValueError('At least one flag is false')
        return True

if __name__ == '__main__':
    validator = FlagValidator()
    print(validator.validate(True, True))
    try:
        print(validator.validate(True, False))
    except ValueError as e:
        print(e)
    try:
        print(validator.validate(False, True))
    except ValueError as e:
        print(e)
    try:
        print(validator.validate(False, False))
    except ValueError as e:
        print(e)