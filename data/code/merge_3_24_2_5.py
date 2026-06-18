class NumberChecker:
    def check_if_negative(self, value):
        """
        Determines if the input value is negative.
        
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
        -5,      # Negative integer
        10,       # Positive integer
        -3.14,   # Negative float
        0,        # Zero (not negative)
        -0.001,  # Small negative number
        2e-5      # Very small positive scientific notation
    ]
    
    for val in test_values:
        result = checker.check_if_negative(val)
        print(f"Value {val} is {'negative' if result else 'non-negative'}")