class NumberChecker:
    @staticmethod
    def is_negative(num):
        return num < 0

if __name__ == '__main__':
    print(NumberChecker.is_negative(-5))
    print(NumberChecker.is_negative(3))
    print(NumberChecker.is_negative(0))
    print(NumberChecker.is_negative(-1.5))