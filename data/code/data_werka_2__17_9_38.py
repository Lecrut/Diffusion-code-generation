class NumberChecker:
    def check_parity(self, number):
        return 'Even' if number % 2 == 0 else 'Odd'

if __name__ == '__main__':
    checker = NumberChecker()
    test_numbers = [10, 33, 56, 77]
    for num in test_numbers:
        result = checker.check_parity(num)
        print(f"The number {num} is {result}.")