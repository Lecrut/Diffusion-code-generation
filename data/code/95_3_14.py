class NumberChecker:
    def is_valid(self, num):
        return num > 0 and num % 2 == 0 and num < 100

if __name__ == '__main__':
    checker = NumberChecker()
    sample_values = [42, -10, 100, 3.14]
    for value in sample_values:
        print(f"{value}: {checker.is_valid(value)}")