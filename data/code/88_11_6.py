class FlagValidator:
    ERROR_MESSAGE = 'At least one flag is false'

    @staticmethod
    def validate_flags(flag1: bool, flag2: bool) -> bool:
        if not (flag1 and flag2):
            raise ValueError(FlagValidator.ERROR_MESSAGE)
        return True

if __name__ == '__main__':
    print(FlagValidator.validate_flags(True, True))
    print(FlagValidator.validate_flags(True, False))
    print(FlagValidator.validate_flags(False, True))