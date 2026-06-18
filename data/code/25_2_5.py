class ValueChecker:
    def check_if_zero(self, value):
        """
        Determines if the input value is zero.
        
        Args:
            value (int | float | None): The numeric value to check.
            
        Returns:
            bool: True if value is 0 or equivalent to 0, False otherwise.
        """
        return value == 0

if __name__ == '__main__':
    checker = ValueChecker()

    # Sample test cases with hard-coded values
    test_values = [
        (5, "positive integer"),
        (-3, "negative integer"),
        (1.0, "float equal to one"),
        (0.0, "float zero"),
        (None, "null value"),
        ("", "empty string"),
    ]

    for val, desc in test_values:
        result = checker.check_if_zero(val)
        print(f"Check {desc} ({val!r}): {'Zero' if result else 'Not Zero'}")