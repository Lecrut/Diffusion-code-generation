class FlagValidator:
    def __init__(self, flag1, flag2):
        self.flag1 = flag1
        self.flag2 = flag2

    def validate_flags(self):
        return self.flag1 and self.flag2

if __name__ == '__main__':
    validator1 = FlagValidator(True, True)
    print(validator1.validate_flags())

    validator2 = FlagValidator(True, False)
    print(validator2.validate_flags())