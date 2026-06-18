class ValueComparator:
    """A class designed to compare two values for inequality."""

    def __init__(self):
        """Initialize the comparator instance without arguments."""
        pass

    def are_unequal(self, value1, value2):
        """
        Compare two values and return True if they are not equal.

        Args:
            value1 (any): The first value to compare.
            value2 (any): The second value to compare.

        Returns:
            bool: True if value1 is not equal to value2, False otherwise.
        """
        return value1 != value2

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    comparator = ValueComparator()

    result_1 = comparator.are_unequal(5, 6)
    print(f"Are 5 and 6 unequal? {result_1}")

    result_2 = comparator.are_unequal("hello", "world")
    print(f"Is 'hello' different from 'world'? {result_2}")

    result_3 = comparator.are_unequal(4.0, 4)
    print(f"Are 4.0 and 4 unequal? {result_3}")

    result_4 = comparator.are_unequal(None, None)
    print(f"Is None different from None? {result_4}")