class NumberChecker:
    """A class to check properties of numbers."""
    
    def check_positivity(self, value):
        """Determine if a number is positive.
        
        Args:
            value (int or float): The numerical value to evaluate.
            
        Returns:
            bool: True if the value is greater than 0, False otherwise.
        """
        return value > 0

if __name__ == '__main__':
    checker = NumberChecker()
    
    # Hard-coded sample values for testing without user input
    test_values = [5, -3, 0, 2.5, float('-inf'), float('inf')]
    
    print("Testing positivity check:")
    for val in test_values:
        result = checker.check_positivity(val)
        status = "Positive" if result else "Not Positive (zero or negative)"
        print(f"{val} -> {status}")