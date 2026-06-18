class NumberChecker:
    """A class to check properties of integers."""
    
    def check_parity(self, number):
        """Determines if an integer is even or odd efficiently.
        
        Args:
            number (int): The integer to be checked for parity.
            
        Returns:
            bool: True if the number is even, False otherwise.
        """
        return not number % 2

if __name__ == '__main__':
    checker = NumberChecker()
    
    # Sample values including positive, negative, and zero
    test_cases = [10, -5, 0, 42]
    
    for num in test_cases:
        result = checker.check_parity(num)
        status = "Even" if result else "Odd"
        print(f"{num} is {status}")