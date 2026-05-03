class NumberChecker:
    def check_if_negative(self, value):
        return value < 0
if __name__ == '__main__':
    checker = NumberChecker()
    sample_values = [10, -5, 0, -100, 3.14]
    for value in sample_values:
        result = checker.check_if_negative(value)
        print(f"Value: {value}, Is Negative: {result}")