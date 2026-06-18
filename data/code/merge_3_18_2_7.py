class ComparisonTool:
    """A utility class to compare internal attributes."""

    def __init__(self, value_a: int = 0, value_b: int = 0):
        """Initialize the tool with two integer values.

        Args:
            value_a (int): The first attribute for comparison.
            value_b (int): The second attribute for comparison.
        """
        self.value_a = value_a
        self.value_b = value_b

    def check_greater(self) -> bool:
        """Check if the internal attribute 'value_a' is strictly greater than 'value_b'.

        Returns:
            bool: True if self.value_a > self.value_b, False otherwise.
        """
        return self.value_a > self.value_b

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files)
    tool = ComparisonTool(value_a=105, value_b=98)

    result = tool.check_greater()
    
    print(f"Comparing {tool.value_a} and {tool.value_b}")
    if result:
        print("Result is True")
    else:
        print("Result is False")