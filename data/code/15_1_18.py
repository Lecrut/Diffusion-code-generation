from typing import Any

class ValueChecker:
    """A utility class to check equality of various data types."""

    def are_equal(self, a: Any, b: Any) -> bool:
        """
        Check if two values are identical.

        This method uses the standard identity operator (__eq__) which works for most
        common Python objects including integers, floats, strings, lists, and dictionaries.
        It returns True if a == b is evaluated as true in Python, otherwise False.

        Args:
            a (Any): The first value to compare.
            b (Any): The second value to compare.

        Returns:
            bool: True if the values are equal, False otherwise.
        """
        return a == b

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    checker = ValueChecker()

    test_cases = [
        (5, 5),              # Integers should be equal
        ("hello", "world"),  # Strings not equal
        ([1, 2], [3, 4]),   # Lists not equal
        ({'key': 'val'}, {'other': True}), # Dictionaries not equal
    ]

    for val_a, val_b in test_cases:
        result = checker.are_equal(val_a, val_b)
        print(f"{type(val_a).__name__}: {result}")