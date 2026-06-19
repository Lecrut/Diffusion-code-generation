class NumberChecker:
    def check_if_negative(self, value):
        return value < 0

if __name__ == '__main__':
    checker = NumberChecker()
    sample_values = [-10, 0, 5, -3.5]
    for value in sample_values:
        print(f"{value}: {checker.check_if_negative(value)}")