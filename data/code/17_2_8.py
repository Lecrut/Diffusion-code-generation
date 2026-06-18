class NumberChecker:
    """A utility class to check mathematical properties of integers."""

    def check_parity(self, number):
        """
        Determines if an integer is even or odd.

        This method uses the modulo operator (%) for efficiency and clarity.
        An even number has a remainder of 0 when divided by 2.
        It accepts both positive and negative integers as well as zero.

        Args:
            number (int): The integer to check.

        Returns:
            str: "Even" if the number is divisible by 2, otherwise "Odd".
        """
        return f"{number} is {'even' if number % 2 == 0 else 'odd'}."

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or files.
    test_values = [10, -5, 42, 0, 7]

    checker = NumberChecker()

    print("Running number parity checks...")
    for val in test_values:
        result = checker.check_parity(val)
        print(result)