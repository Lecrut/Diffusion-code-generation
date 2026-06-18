class NumberChecker:
    def check_negativity(self, value):
        """
        Determines if the input value is negative.
        
        Args:
            value (int or float): The number to check.
            
        Returns:
            bool: True if the value is strictly less than zero, False otherwise.
        """
        return isinstance(value, (int, float)) and value < 0

if __name__ == '__main__':
    checker = NumberChecker()

    # Sample test cases with hard-coded values
    test_values = [
        -5,      # Negative integer -> True
        -3.14,   # Negative float -> True
        0,       # Zero -> False (not negative)
        10,      # Positive int -> False
        2.718,   # Positive float -> False
    ]

    for val in test_values:
        result = checker.check_negativity(val)
        print(f"Is {val} negative? {result}")