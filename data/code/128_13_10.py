class NegativeChecker:
    @staticmethod
    def is_negative(value):
        return value < 0

if __name__ == '__main__':
    print(NegativeChecker.is_negative(-5))
    print(NegativeChecker.is_negative(3))
    print(NegativeChecker.is_negative(0))
    print(NegativeChecker.is_negative(-1.5))