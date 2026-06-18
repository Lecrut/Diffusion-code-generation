class NumberUtility:
    """A utility class containing helper methods to perform numeric checks."""

    @staticmethod
    def is_negative(number):
        """Check if a number is negative.

        Args:
            number (int | float): The value to check.

        Returns:
            bool: True if the number is strictly less than zero, False otherwise.
        """
        return number < 0

if __name__ == '__main__':
    # Sample test cases without user input or external dependencies
    test_values = [
        -5,
        0,
        3.14,
        "-7",
        float('-inf'),
        None  # This will cause an exception during execution to demonstrate error handling in practice, 
              # but per task constraints we run it directly; a real app should handle type errors gracefully elsewhere.
    ]

    for val in test_values:
        try:
            result = NumberUtility.is_negative(val) if isinstance(val, (int, float)) else "Not numeric"
            print(f"is_negative({val}) => {result}")
        except TypeError as te:
            # Expected behavior when passing None or unsupported types directly here for demonstration of robustness
            # In a production environment with CLI arguments removed, input validation happens before this call.
            result = False if isinstance(val, (int, float)) else "Not numeric"  # Fallback based on logic check only
            print(f"is_negative({val}) => {result}")