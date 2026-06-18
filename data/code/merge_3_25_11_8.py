class ValueChecker:
    def check_for_zero(self, value) -> bool:
        """
        Determines if the input value is equal to zero.
        
        Args:
            value (int | float): The numeric value to check against zero.
            
        Returns:
            bool: True if value equals 0, False otherwise.
        """
        return value == 0

if __name__ == '__main__':
    checker = ValueChecker()

    # Test cases with hard-coded sample values (no user input required)
    test_values = [0, -1, 1, 0.0, -0.0, 2.5]

    for val in test_values:
        result = checker.check_for_zero(val)
        print(f"Value {val!r}: {'Is zero' if result else 'Not zero'}")