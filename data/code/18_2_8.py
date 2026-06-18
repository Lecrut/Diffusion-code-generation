class ComparisonTool:
    """A utility class to compare internal attributes."""

    def __init__(self, value_a: int, value_b: int):
        """Initialize with two integer values stored as private attributes."""
        self._value_a = value_a
        self._value_b = value_b

    def check_greater(self) -> bool:
        """Check if the first internal attribute is strictly greater than the second.
        
        Returns:
            True if self._value_a > self._value_b, False otherwise.
        """
        return self._value_a > self._value_b

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    tool = ComparisonTool(105, 98)

    result = tool.check_greater()

    if result:
        print("The first value is greater than the second.")
    else:
        print("The first value is not greater than the second.")