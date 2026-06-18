class ValueChecker:
    """A class designed to check if a given value is zero."""

    def check_if_zero(self, value):
        """
        Determines if the input value is equal to zero.

        Args:
            value (int | float | None): The value to be checked.

        Returns:
            bool: True if the value is zero, False otherwise.
        
        Examples:
            checker = ValueChecker()
            print(checker.check_if_zero(0))   # Output: True
            print(checker.check_if_zero(-1))  # Output: False
        """
        return value == 0

if __name__ == '__main__':
    checker = ValueChecker()

    sample_values = [0, -5, 3.14, None]
    
    for val in sample_values:
        result = checker.check_if_zero(val)
        print(f"Value {val!r} is zero? {result}")