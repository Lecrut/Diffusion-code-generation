from __future__ import annotations

class ValueChecker:
    """A class to check if two provided values are unequal."""

    def is_unequal(self, value1: Any, value2: Any) -> bool:
        """
        Determine if the given two values are not equal.

        Args:
            value1 (Any): The first value to compare.
            value2 (Any): The second value to compare.

        Returns:
            bool: True if value1 is not equal to value2, False otherwise.
        """
        return value1 != value2

if __name__ == '__main__':
    checker = ValueChecker()

    # Sample test cases with hard-coded values
    assert checker.is_unequal(5, 3) is True
    assert checker.is_unequal("hello", "world") is True
    assert checker.is_unequal([1, 2], [3, 4]) is True
    assert checker.is_unequal(None, False) is True

    # Edge cases where values are equal (should return False for unequal check)
    assert checker.is_unequal(5, 5) is False
    assert checker.is_unequal("test", "test") is False
    assert checker.is_unequal([1], [1]) is False

    print("All sample checks passed.")