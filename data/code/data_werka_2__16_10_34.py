class PositiveChecker:
    @staticmethod
    def is_positive(x):
        return x > 0

if __name__ == '__main__':
    print(PositiveChecker.is_positive(7))
    print(PositiveChecker.is_positive(-2))
    print(PositiveChecker.is_positive(0))