class ComparisonTool:
    """A utility class for comparing internal attributes."""

    def __init__(self, value_a: int = 10, value_b: int = 5):
        """Initialize the tool with two integer values to compare.

        Args:
            value_a (int): The first value to be compared. Defaults to 10.
            value_b (int): The second value to be compared. Defaults to 5.
        """
        self.value_a = value_a
        self.value_b = value_b

    def check_greater(self) -> bool:
        """Check if the internal attribute 'value_a' is strictly greater than 'value_b'.

        Returns:
            bool: True if value_a > value_b, otherwise False.
        """
        return self.value_a > self.value_b

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    tool = ComparisonTool(value_a=20, value_b=15)

    result = tool.check_greater()

    if result:
        print("The first attribute is greater than the second.")
    else:
        print("The first attribute is not greater than the second.")