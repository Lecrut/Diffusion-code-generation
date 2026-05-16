class ValueChecker:
    def check_for_zero(self, value):
        return value == 0
if __name__ == '__main__':
    checker = ValueChecker()
    sample_values = [0, 5, -3, 0.0, 100]
    for value in sample_values:
        result = checker.check_for_zero(value)
        print(f"Value: {value}, Is Zero: {result}")