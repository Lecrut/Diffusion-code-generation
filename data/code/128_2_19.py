class NumberChecker:
    def check_negativity(self, value):
        return value < 0

if __name__ == '__main__':
    checker = NumberChecker()
    sample_values = [10.5, -3.2, 0.0, -100.1, 3.14]
    for value in sample_values:
        result = checker.check_negativity(value)
        print(f"Value: {value}, Is Negative: {result}")