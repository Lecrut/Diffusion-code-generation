class ValueChecker:
    """A utility class to compare two values efficiently."""

    def __init__(self):
        pass

    def are_different(self, val1, val2):
        """
        Check if the provided values are not equal.

        Args:
            val1 (any): The first value to compare.
            val2 (any): The second value to compare.

        Returns:
            bool: True if val1 is not equal to val2, False otherwise.
        """
        return val1 != val2

if __name__ == '__main__':
    checker = ValueChecker()

    # Sample test cases with hard-coded values
    assert checker.are_different(5, 3) is True
    assert checker.are_different("hello", "world") is True
    assert checker.are_different([1, 2], [1]) is True
    assert checker.are_different(True, False) is True

    # Test cases where values are equal
    assert checker.are_different(5, 5) is False
    assert checker.are_different("hello", "hello") is False
    assert checker.are_different([1, 2], [1, 2]) is False
    assert checker.are_different(True, True) is False

    print("All tests passed.")