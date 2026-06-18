class NumberChecker:
    """A class to check properties of numeric values."""
    
    def check_negativity(self, value):
        """
        Determines if the given input value is negative.
        
        Parameters:
            value (int or float): The number to check.
            
        Returns:
            bool: True if value is strictly less than zero, False otherwise.
        """
        return value < 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    test_values = [
        -5,     # Should be negative
        0,      # Not negative (zero)
        3.14,   # Positive float
        None,   # Will raise TypeError as expected with built-in comparison
        "abc",  # Will raise TypeError as expected
    ]

    checker = NumberChecker()

    for val in test_values:
        try:
            result = checker.check_negativity(val)
            print(f"Value {val} is negative? {result}")
        except TypeError:
            print(f"Value {val} cannot be compared (non-numeric)")