class ValueComparator:
    """A class designed to compare two values for inequality."""

    def __init__(self):
        """Initialize the comparator instance with no arguments needed."""
        pass

    @staticmethod
    def are_unequal(value1, value2):
        """
        Compare two arguments and return True if they are not equal.

        This method handles various types by attempting comparison directly,
        which works for numbers, strings, lists, tuples, etc., in Python 3.
        It avoids type-specific checks to maintain simplicity while being robust.

        Args:
            value1 (any): The first value to compare.
            value2 (any): The second value to compare.

        Returns:
            bool: True if the values are not equal, False otherwise.
        """
        return value1 != value2

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    comparator = ValueComparator()

    tests = [
        (5, 3),           # Should be True
        "hello", "world", # Should be True
        [1, 2], [1, 2],  # Should be False
        (4.0, 4),         # Should be False (float equality)
        None, None,       # Should be False
    ]

    for val1, val2 in tests:
        result = comparator.are_unequal(val1, val2)
        print(f"are_unequal({val1!r}, {val2!r}) -> {result}")