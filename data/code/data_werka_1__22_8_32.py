class NumberChecker:

    def check_odd(self, number):
        return number % 2 != 0
if __name__ == '__main__':
    checker = NumberChecker()
    test_values = [10, 15, -2, 3, 0]
    for value in test_values:
        result = checker.check_odd(value)
        print(f'The number {value} is odd: {result}')