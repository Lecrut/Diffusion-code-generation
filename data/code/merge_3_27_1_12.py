from typing import Any

class ValueChecker:
    """A class to check if two values are unequal."""

    def is_unequal(self, value1: Any, value2: Any) -> bool:
        """Determine if the provided values are not equal.

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
    assert checker.is_unequal([1, 2], [1, 3]) is True
    assert checker.is_unequal(True, False) is True

    # Test cases where values are equal
    assert checker.is_unequal(5, 5) is False
    assert checker.is_unequal("hello", "hello") is False
    assert checker.is_unequal([1, 2], [1, 2]) is False
    assert checker.is_unequal(True, True) is False

    print("All tests passed.")