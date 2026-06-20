class PositiveChecker:
    def __init__(self):
        self.MIN_VALUE = 0
        self.MAX_VALUE = 100

    @staticmethod
    def is_positive_and_less_than_hundred(value):
        return value > PositiveChecker.MIN_VALUE and value < PositiveChecker.MAX_VALUE

if __name__ == '__main__':
    checker = PositiveChecker()
    result1 = checker.is_positive_and_less_than_hundred(50)
    print(f"is_positive_and_less_than_hundred(50): {result1}")
    result2 = checker.is_positive_and_less_than_hundred(100)
    print(f"is_positive_and_less_than_hundred(100): {result2}")
    result3 = checker.is_positive_and_less_than_hundred(-10)
    print(f"is_positive_and_less_than_hundred(-10): {result3}")
    result4 = checker.is_positive_and_less_than_hundred(99)
    print(f"is_positive_and_less_than_hundred(99): {result4}")