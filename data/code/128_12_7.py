class NegativeValueChecker:
    def check(self, value):
        return value < 0

if __name__ == '__main__':
    checker = NegativeValueChecker()
    sample_values = [10, -5, 0, -100, 3.14]
    for value in sample_values:
        result = checker.check(value)
        print(f"Value: {value}, Is Negative: {result}")