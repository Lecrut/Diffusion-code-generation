class NumberChecker:
    """A class to check properties of integers."""
    
    def check_odd(self, number):
        """Check if a given integer is odd.
        
        Args:
            number (int): The integer to be checked.
            
        Returns:
            bool: True if the number is odd, False otherwise.
        """
        return number % 2 != 0

if __name__ == '__main__':
    checker = NumberChecker()

    # Sample test cases with hard-coded values
    sample_values = [1, 4, -3, 0, 9]

    for val in sample_values:
        result = checker.check_odd(val)
        print(f"{val} is {'odd' if result else 'even'}")