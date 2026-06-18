class NumberChecker:
    def check_positivity(self, value):
        """
        Determines if the input value is strictly positive (greater than zero).
        
        Args:
            value (int or float): The number to evaluate.
            
        Returns:
            bool: True if value > 0, False otherwise.
        """
        return value > 0

if __name__ == '__main__':
    checker = NumberChecker()
    
    # Hard-coded sample values for testing without user input or external dependencies
    test_values = [5, -3, 0, 2.5, float('inf'), float('-inf')]
    
    print("Testing NumberChecker.check_positivity:")
    for val in test_values:
        result = checker.check_positivity(val)
        status = "Positive" if result else "Non-positive (zero or negative)"
        # Handle special floats cleanly by converting to string representation without printing raw float objects directly in a way that breaks readability, 
        # though Python's default str() handles inf nicely.
        print(f"Value: {val!r} -> {status}")