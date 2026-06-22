class NumberChecker:
    def check_positivity(self, value):
        return value > 0

if __name__ == '__main__':
    checker = NumberChecker()
    sample_values = [10, -5, 0, 23.5, -100]
    for value in sample_values:
        print(f"{value} is positive: {checker.check_positivity(value)}")