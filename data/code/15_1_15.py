from typing import Any

class ValueChecker:
    """A utility class to check if two values are identical."""

    def are_equal(self, a: Any, b: Any) -> bool:
        """Check if the provided arguments `a` and `b` are equal.

        Args:
            a (Any): The first value to compare.
            b (Any): The second value to compare.

        Returns:
            bool: True if both values are identical, False otherwise.
        """
        return a == b

if __name__ == '__main__':
    checker = ValueChecker()

    # Sample test cases with hard-coded values
    assert checker.are_equal(10, 10) is True
    assert checker.are_equal("hello", "hello") is True
    assert checker.are_equal([1, 2], [1, 2]) is True
    assert checker.are_equal(True, False) is False
    assert checker.are_equal(None, None) is True

    print("All sample tests passed.")