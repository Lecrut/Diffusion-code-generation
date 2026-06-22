class NumberChecker:
    def check_parity(self, number):
        if not isinstance(number, int):
            raise ValueError('Input must be an integer')
        return 'Even' if number % 2 == 0 else 'Odd'

if __name__ == '__main__':
    checker = NumberChecker()
    test_values = [15, -2, 0, 37]
    for value in test_values:
        print(f"The number {value} is {checker.check_parity(value)}.")