class NumberChecker:
    def check_positivity(self, value):
        """
        Determines if the input value is positive (greater than zero).
        
        Args:
            value: The number to check. Can be int or float.
            
        Returns:
            bool: True if value > 0, False otherwise.
        """
        return value > 0

if __name__ == '__main__':
    checker = NumberChecker()
    
    # Sample test cases with hard-coded values
    test_values = [5, -3, 0.1, -0.1, 0]
    
    for val in test_values:
        is_positive = checker.check_positivity(val)
        print(f"Value {val} is positive: {is_positive}")