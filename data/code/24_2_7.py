class NumberChecker:
    def check_if_negative(self, value):
        """
        Determines if a given numeric value is negative.
        
        Args:
            value (int or float): The number to check.
            
        Returns:
            bool: True if the value is less than zero, False otherwise.
        """
        return value < 0

if __name__ == '__main__':
    checker = NumberChecker()
    
    # Sample test cases with hard-coded values
    test_values = [
        -5,     # Should be negative
        10,      # Positive
        0.0,     # Zero (not negative)
        -3.14,   # Negative float
        2e-5,    # Small positive number in scientific notation
        -7 * 10 ** 6  # Large negative integer
    ]
    
    for val in test_values:
        result = checker.check_if_negative(val)
        print(f"Value: {val} -> Is Negative: {result}")