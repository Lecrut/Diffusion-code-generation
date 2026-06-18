class NumberChecker:
    """A utility class to check properties of numeric values."""
    
    def check_if_negative(self, value):
        """
        Determines if the input value is negative.
        
        Args:
            value (int | float): The numerical value to evaluate.
            
        Returns:
            bool: True if value < 0, False otherwise.
        """
        return value < 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or network access
    checker = NumberChecker()

    test_cases = [
        -5,      # Negative integer
        -3.14,   # Negative float
        0,       # Zero (non-negative)
        10,      # Positive integer
        2.718,   # Positive float
        None     # Edge case: non-numeric input handled by exception expected behavior or just checking types
    ]

    for test_val in test_cases:
        try:
            if isinstance(test_val, (int, float)) and not isinstance(test_val, bool):
                result = checker.check_if_negative(test_val)
                print(f"Value {test_val} is negative: {result}")
            else:
                # If the input isn't a valid number for this check, we skip or handle appropriately.
                # For strict 'is it negative' logic, non-numbers are neither strictly positive nor negative in math context usually.
                print(f"Value {test_val} is not a numeric type suitable for direct negativity check.")
        except Exception as e:
            print(f"Error checking value {test_val}: {e}")