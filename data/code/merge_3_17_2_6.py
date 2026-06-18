class NumberChecker:
    """A class to perform basic numerical checks on integers."""

    def check_parity(self, number):
        """
        Determines if an integer is even or odd.
        
        Args:
            number (int): The integer to be checked for parity.
            
        Returns:
            bool: True if the number is even, False otherwise.
        """
        return number % 2 == 0

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    test_values = [10, -5, 7, 42]

    checker = NumberChecker()

    for val in test_values:
        result = checker.check_parity(val)
        print(f"Number {val} is {'even' if result else 'odd'}")