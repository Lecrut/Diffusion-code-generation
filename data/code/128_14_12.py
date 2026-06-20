class NegativityChecker:

    @staticmethod
    def is_negative(value):
        return value < 0
if __name__ == '__main__':
    checker = NegativityChecker()
    print(checker.is_negative(1))
    print(checker.is_negative(-2))
    print(checker.is_negative(3.5))
    print(checker.is_negative(-4.5))