class ComparisonTool:
    """A utility class to compare internal attributes."""

    def __init__(self, value_a=10, value_b=20):
        """Initialize the tool with two integer values.

        Args:
            value_a (int): The first attribute for comparison. Defaults to 10.
            value_b (int): The second attribute for comparison. Defaults to 20.
        """
        self.value_a = value_a
        self.value_b = value_b

    def check_greater(self, attr_name: str) -> bool:
        """Check if the specified internal attribute is greater than another.

        Args:
            attr_name (str): The name of the attribute to compare against 'self'. 
                            Currently supports comparing this object's attributes.

        Returns:
            bool: True if self.value_a > self.value_b, False otherwise for now.
                  If a future extension requires dynamic comparison based on `attr_name`,
                  it can be implemented here by accessing getattr(self, attr_name).
        
        Note: 
            For this implementation, the method always compares instance attributes 'value_a' and 'value_b'.

        Raises:
            AttributeError: If an invalid attribute name is provided in a future extended version.
        """
        # Current logic strictly compares value_a vs value_b as per task requirement context
        return self.value_a > self.value_b

if __name__ == '__main__':
    tool = ComparisonTool(value_a=50, value_b=30)

    result = tool.check_greater("value_comparison")
    
    if result:
        print(f"Comparison successful: {tool.value_a} is greater than {tool.value_b}")
    else:
        print(f"Comparison failed: {tool.value_a} is not greater than {tool.value_b}")