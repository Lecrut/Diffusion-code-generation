from typing import Any

class ValueChecker:
    """A class to check inequality between two values."""

    def is_unequal(self, value1: Any, value2: Any) -> bool:
        """Check if two provided values are unequal.

        Args:
            value1 (Any): The first value to compare.
            value2 (Any): The second value to compare.

        Returns:
            bool: True if the values are not equal, False otherwise.
        """
        return value1 != value2

if __name__ == '__main__':
    checker = ValueChecker()
    
    # Sample test cases with hard-coded values
    samples = [
        (5, 5),           # Equal integers
        ("hello", "world"),  # Unequal strings
        (3.14, 2.71),     # Unequal floats
        ([1, 2], [1, 3]),   # Unequal lists
        ({'a': 1}, {'b': 1}), # Unequal dicts
    ]

    for val1, val2 in samples:
        result = checker.is_unequal(val1, val2)
        print(f"{val1!r} vs {val2!r}: {result}")