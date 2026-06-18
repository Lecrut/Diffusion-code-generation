class NumberChecker:
    def check_positivity(self, value):
        """
        Determines if the input value is positive (strictly greater than zero).
        
        Args:
            value: The numeric value to check. Can be int or float.
            
        Returns:
            bool: True if value > 0, False otherwise.
        """
        return isinstance(value, (int, float)) and value > 0

if __name__ == '__main__':
    checker = NumberChecker()
    
    # Sample test cases with hard-coded values
    test_values = [5, -3, 0, 2.5, -1e-10]
    
    for val in test_values:
        result = checker.check_positivity(val)
        print(f"Is {val} positive? {result}")