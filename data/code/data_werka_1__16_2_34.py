class PositiveChecker:
    def is_positive(self, value):
        return value > 0

if __name__ == '__main__':
    checker = PositiveChecker()
    test_values = [42, -17, 0, 2.718, -0.99]
    for value in test_values:
        result = checker.is_positive(value)
        print(f"Is {value} positive? {'Yes' if result else 'No'}")