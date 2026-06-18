class NumberChecker:
    """A class to perform basic numerical checks on integers."""

    def check_parity(self, number):
        """
        Determines if an integer is even or odd.

        Args:
            number (int): The integer to be checked.

        Returns:
            bool: True if the number is even, False otherwise.
        """
        return number % 2 == 0

if __name__ == '__main__':
    checker = NumberChecker()
    
    # Sample values for testing without user input or external dependencies
    test_values = [10, -4, 7, 0, 3.5]

    print("Testing parity check:")
    for val in test_values:
        if isinstance(val, int):
            is_even = checker.check_parity(val)
            status = "Even" if is_even else "Odd"
            print(f"{val} -> {status}")
        else:
            print(f"{val} -> Not an integer")