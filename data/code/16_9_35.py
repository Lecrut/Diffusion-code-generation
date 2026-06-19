class NumberChecker:
    def check_positivity(self, value):
        return value > 0

if __name__ == '__main__':
    checker = NumberChecker()
    sample_values = [10, -5, 0, 23.4, -17.8]
    for value in sample_values:
        result = checker.check_positivity(value)
        print(f"The number {value} is positive: {result}")