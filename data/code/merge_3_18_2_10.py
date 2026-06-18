class ComparisonTool:
    """A utility class to compare internal attributes."""

    def __init__(self, value_a: int = 10, value_b: int = 5):
        """Initialize the tool with two integer values for comparison.

        Args:
            value_a (int): The first attribute value. Defaults to 10.
            value_b (int): The second attribute value. Defaults to 5.
        """
        self.value_a = value_a
        self.value_b = value_b

    def check_greater(self) -> bool:
        """Check if the internal attribute 'value_a' is strictly greater than 'value_b'.

        Returns:
            bool: True if self.value_a > self.value_b, otherwise False.
        """
        return self.value_a > self.value_b

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    tool = ComparisonTool(value_a=100, value_b=50)

    result = tool.check_greater()

    if result:
        print("The first attribute is greater than the second.")
    else:
        print("The first attribute is not greater than the second.")