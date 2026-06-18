class NumberChecker:
    """A class that checks properties of integers."""

    def check_parity(self, number):
        """
        Determines if an integer is even.
        
        Args:
            number (int): The integer to be checked.
            
        Returns:
            bool: True if the number is even, False otherwise.
        """
        return number % 2 == 0

if __name__ == '__main__':
    checker = NumberChecker()

    # Hard-coded sample values for testing without user input or external dependencies
    test_values = [10, -5, 42, -8]

    print("Testing 'NumberChecker.check_parity' method:\n")

    for value in test_values:
        is_even = checker.check_parity(value)
        status = "Even" if is_even else "Odd"
        print(f"{value}: {status}")