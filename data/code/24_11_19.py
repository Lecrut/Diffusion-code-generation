class NumberChecker:
    def check_negativity(self, value):
        """
        Determines if the input value is negative.
        
        Args:
            value (int or float): The number to check.
            
        Returns:
            bool: True if value < 0, False otherwise.
        """
        return value < 0

if __name__ == '__main__':
    checker = NumberChecker()
    
    # Sample test cases with hard-coded values
    test_values = [
        -5,      # Negative integer
        0,       # Zero (not negative)
        -3.14,   # Negative float
        42,      # Positive integer
        -0.001,  # Small negative float
        None     # Edge case: should raise TypeError as per standard behavior for numeric checks
    ]
    
    print("Testing NumberChecker.check_negativity():")
    for val in test_values[:-1]:  # Skip None to avoid runtime error during demo output unless handled
        result = checker.check_negativity(val)
        status = "Negative" if result else "Non-negative"
        print(f"Value: {val} -> Status: {status}")
    
    # Demonstrate exception handling for non-numeric input (optional but good practice)
    try:
        is_negative = checker.check_negativity(None)
    except TypeError as e:
        print(f"\nHandling invalid type 'None': Error occurred - {e}")