class NumberChecker:
    def check_positivity(self, value):
        """
        Determines if the input value is positive (strictly greater than zero).
        
        Args:
            value: The number to check. Can be int or float.
            
        Returns:
            bool: True if value > 0, False otherwise.
        """
        return value > 0

if __name__ == '__main__':
    checker = NumberChecker()
    
    # Hard-coded sample values for testing without user input
    test_values = [10, -5, 0, 3.14, float('inf'), float('-inf')]
    
    print("Testing NumberChecker.check_positivity():")
    for val in test_values:
        result = checker.check_positivity(val)
        status = "Positive" if result else "Non-positive (zero or negative)"
        print(f"{val}: {status}")