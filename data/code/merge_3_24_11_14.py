class NumberChecker:
    """A class to check properties of numbers."""
    
    def check_negativity(self, value):
        """Determines if the input value is negative.
        
        Args:
            value: The numeric value to check (int or float).
            
        Returns:
            bool: True if the value is strictly less than zero, False otherwise.
        """
        return isinstance(value, (int, float)) and value < 0

if __name__ == '__main__':
    checker = NumberChecker()
    
    # Sample values to test without user input or network access
    sample_values = [10, -5.5, 0, "negative", False]

    for val in sample_values:
        result = checker.check_negativity(val)
        print(f"Value: {val}, Is negative: {result}")