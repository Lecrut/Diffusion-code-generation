class ComparisonTool:
    """A utility class to compare internal attributes."""

    def __init__(self, value_a=0, value_b=1):
        """Initialize with two optional integer values."""
        self.value_a = value_a
        self.value_b = value_b

    def check_greater(self) -> bool:
        """Check if the first attribute is greater than the second.

        Returns:
            True if self.value_a > self.value_b, False otherwise.
        """
        return self.value_a > self.value_b

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input)
    tool = ComparisonTool(value_a=10, value_b=5)

    result = tool.check_greater()

    if result:
        print("The first attribute is greater than the second.")
    else:
        print("The first attribute is not greater than the second.")