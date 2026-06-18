class NumberChecker:
    def check_parity(self, number):
        """Returns 'Even' if the number is even, otherwise returns 'Odd'."""
        return "Even" if number % 2 == 0 else "Odd"

if __name__ == '__main__':
    checker = NumberChecker()

    # Sample values to test without user input or external dependencies
    sample_numbers = [4, 7, -3, 10]

    for num in sample_numbers:
        result = checker.check_parity(num)
        print(f"{num} is {result}")