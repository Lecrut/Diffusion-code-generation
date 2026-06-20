class NegativeValueChecker:
    @staticmethod
    def is_negative(value):
        return value < 0

if __name__ == '__main__':
    checker = NegativeValueChecker()
    print(checker.is_negative(-5))
    print(checker.is_negative(3))
    print(checker.is_negative(0))