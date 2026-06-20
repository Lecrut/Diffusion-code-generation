class PositiveChecker:
    def is_positive_and_less_than_100(self, value: float) -> bool:
        return 0 < value < 100

if __name__ == '__main__':
    checker = PositiveChecker()
    sample_values = [50, -1, 100, 101, 0.99]
    for value in sample_values:
        result = checker.is_positive_and_less_than_100(value)
        print(f"is_positive_and_less_than_100({value}) is: {result}")