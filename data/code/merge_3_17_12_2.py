class NumberChecker:
    def check_parity(self, number):
        """
        Checks if a given integer is even or odd.

        Args:
            number (int): The integer to be checked.

        Returns:
            str: 'Even' if the number is divisible by 2, otherwise 'Odd'.
        """
        return "Even" if number % 2 == 0 else "Odd"

if __name__ == '__main__':
    checker = NumberChecker()

    # Hard-coded sample values for testing without user input
    test_numbers = [4, 7, -3, 10]

    print("Parity Check Results:")
    for num in test_numbers:
        result = checker.check_parity(num)
        print(f"Number {num} is {result}")