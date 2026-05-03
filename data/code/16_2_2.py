class NumberChecker:
    def check_positivity(self, value):
        return value > 0
if __name__ == '__main__':
    checker = NumberChecker()
    test_values = [10, -5, 0, 3.14, -0.001]
    for value in test_values:
        result = checker.check_positivity(value)
        print(f"Is {value} positive? {result}")