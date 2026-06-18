from typing import Any

class ValueChecker:
    """A class providing utilities to check value equality."""

    def __init__(self) -> None:
        """Initialize the ValueChecker instance."""
        pass

    @staticmethod
    def are_equal(a: Any, b: Any) -> bool:
        """
        Check if two input values are identical.

        Args:
            a (Any): The first value to compare.
            b (Any): The second value to compare.

        Returns:
            bool: True if the values are equal and both exist, False otherwise.
        """
        return a == b

if __name__ == '__main__':
    checker = ValueChecker()

    # Sample test cases with hard-coded values
    sample_cases = [
        (5, 5),          # Should be True
        ("hello", "world"),  # Should be False
        ([1, 2], [1, 2]),   # Should be True
        ([1, 2], [3, 4]),   # Should be False
        (None, None),     # Should be True
        ({}, {}),         # Should be True (empty dicts are equal)
    ]

    for i, (item_a, item_b) in enumerate(sample_cases):
        result = checker.are_equal(item_a, item_b)
        print(f"Test case {i + 1}: ValueChecker.are_equal({repr(item_a)}, {repr(item_b)}) -> {result}")