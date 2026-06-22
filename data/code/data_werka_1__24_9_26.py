class NumberChecker:
    def check_negativity(self, value):
        return value < 0

if __name__ == '__main__':
    checker = NumberChecker()
    sample_values = [10, -20, 0, -5.5, 3]
    for value in sample_values:
        print(f"{value} is negative: {checker.check_negativity(value)}")