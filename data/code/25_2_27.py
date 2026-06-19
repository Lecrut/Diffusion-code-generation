class ValueChecker:
    def check_if_zero(self, value):
        return value == 0

if __name__ == '__main__':
    checker = ValueChecker()
    sample_values = [0, 1, -1, 2.5, None]
    for val in sample_values:
        result = checker.check_if_zero(val)
        print(f"Is {val} zero? {result}")