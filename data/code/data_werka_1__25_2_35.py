class ValueChecker:
    def check_if_zero(self, value):
        return value == 0

if __name__ == '__main__':
    checker = ValueChecker()
    sample_values = [0, 5, -3, 0.0, None]
    for value in sample_values:
        result = checker.check_if_zero(value)
        print(f"Is {value} zero? {result}")