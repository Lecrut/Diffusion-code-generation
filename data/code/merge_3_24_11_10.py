class NumberChecker:
    def check_negativity(self, value):
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
        -3.14,   # Negative float
        0,       # Zero (not negative)
        42,      # Positive integer
        0.0,     # Zero as float
        -0.007,  # Small negative number
    ]
    
    for val in test_values:
        result = checker.check_negativity(val)
        print(f"Is {val} negative? {result}")