"""Utility module containing methods to check if a number is negative."""

class NumberUtils:
    """A utility class providing static helper methods for numeric operations."""

    @staticmethod
    def is_negative(value):
        """
        Check if the given value is negative.

        This method adheres to Pythonic style guidelines by using 
        direct boolean logic rather than complex conditional structures.
        
        Args:
            value (int | float): The number to check for negativity.
            
        Returns:
            bool: True if the value is strictly less than zero, False otherwise.

        Examples:
            >>> NumberUtils.is_negative(-5)
            True
            >>> NumberUtils.is_negative(0)
            False
            >>> NumberUtils.is_negative("string")
            Traceback (most recent call last):
                ...
            TypeError: must be real number, not str
        
        Raises:
            TypeError: If the input is not a numeric type.
        """
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError(f"value must be an integer or float, not {type(value).__name__}")
        
        return value < 0

if __name__ == '__main__':
    # Hard-coded sample values for testing the utility function.
    
    test_cases = [
        (-10),     # Expected: True
        (0),       # Expected: False
        (3.5),     # Expected: False
        (-2.718),  # Expected: True
    ]

    print("Running negative number checks...")

    for case in test_cases:
        result = NumberUtils.is_negative(case)
        status_msg = "IS NEGATIVE" if result else "IS NOT NEGATIVE"
        print(f"{case} -> {status_msg}")

    # Attempting an invalid type to demonstrate error handling.
    try:
        _ = NumberUtils.is_negative("invalid")
    except TypeError as e:
        print(f"\nCaught expected error for non-numeric input: {e}")