class NumberChecker:
    def check_parity(self, number):
        """Returns 'Even' if the number is even, otherwise returns 'Odd'."""
        return "Even" if number % 2 == 0 else "Odd"

if __name__ == '__main__':
    checker = NumberChecker()

    # Sample test cases with hard-coded values
    test_values = [10, 7, -4, 0]

    for val in test_values:
        result = checker.check_parity(val)
        print(f"{val} is {result}")