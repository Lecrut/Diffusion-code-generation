class ComparisonTool:
    """A utility class to compare internal attributes."""

    def __init__(self, value1, value2):
        """Initialize with two comparable values stored as private attributes."""
        self._value1 = value1
        self._value2 = value2

    @staticmethod
    def check_greater(val_a: object, val_b: object) -> bool:
        """
        Compare two values and return True if the first is strictly greater than the second.

        Args:
            val_a (object): First value to compare.
            val_b (object): Second value to compare.

        Returns:
            bool: True if val_a > val_b, otherwise False.
        """
        try:
            return val_a > val_b
        except TypeError:
            # Gracefully handle types that cannot be compared directly
            return False

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    tool = ComparisonTool(10, 5)

    result_1 = tool._value1 > tool._value2
    print(f"Is {tool._value1} greater than {tool._value2}? {result_1}")

    # Test the static method directly with mixed types to ensure robustness
    sample_result = ComparisonTool.check_greater("hello", "hi")
    print(f"'hello' > 'hi'? {sample_result}")  # Should be False because len('hello') < len('hi') in lexicographical comparison? Actually, string compare is char by char. 'h' == 'h', then 'e' vs 'i'. ASCII of e (101) < i (105). So "hello" > "hi" is False.

    # Test with numbers
    tool2 = ComparisonTool(3.14, 2.71)
    result_2 = tool2._value1 > tool2._value2
    print(f"Is {tool2._value1} greater than {tool2._value2}? {result_2}")

    # Test with equal values
    tool3 = ComparisonTool(42, 42)
    result_3 = tool3._value1 > tool3._value2
    print(f"Is {tool3._value1} greater than {tool3._value2}? {result_3}")

    # Test with incompatible types (int vs string might raise TypeError in comparison context usually, handled by static method)
    result_incompatible = ComparisonTool.check_greater(42, "text")
    print(f"Is 42 > 'text'? {result_incompatible}")