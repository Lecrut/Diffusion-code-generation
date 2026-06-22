class NumberChecker:
    def check_odd(self, number):
        return number % 2 != 0

if __name__ == '__main__':
    checker = NumberChecker()
    sample_values = [1, 2, 3, 4, 5]
    for value in sample_values:
        result = checker.check_odd(value)
        print(f"{value} is odd: {result}")