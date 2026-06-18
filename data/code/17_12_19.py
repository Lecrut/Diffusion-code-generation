class NumberChecker:
    def check_parity(self, number):
        """Returns 'Even' if the number is even, otherwise returns 'Odd'."""
        return "Even" if number % 2 == 0 else "Odd"

if __name__ == '__main__':
    checker = NumberChecker()

    # Sample values to test without user input or network access
    samples = [10, -3, 42, 0]

    for num in samples:
        result = checker.check_parity(num)
        print(f"{num} is {result}")