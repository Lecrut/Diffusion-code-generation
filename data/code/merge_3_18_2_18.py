class ComparisonTool:
    """A utility class to compare internal attributes."""

    def __init__(self, value_a, value_b):
        """Initialize the tool with two values to be compared internally.

        Args:
            value_a (any comparable type): The first attribute/value.
            value_b (any comparable type): The second attribute/value.
        """
        self._value_a = value_a
        self._value_b = value_b

    def check_greater(self) -> bool:
        """Check if the internal attribute 'a' is strictly greater than 'b'.

        Returns:
            bool: True if self.value_a > self.value_b, False otherwise.
        """
        return self._value_a > self._value_b

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    tool = ComparisonTool(100, 50)

    print(tool.check_greater())  # Expected output: True