from typing import Any

class ValueChecker:
    """A utility class to check if two values are identical."""

    @staticmethod
    def are_equal(a: Any, b: Any) -> bool:
        """Check if the two input values are identical.

        This method uses the `is` operator for identity checks in Python 3,
        which is more efficient than using `==` for certain types like integers
        and strings due to interning mechanisms. However, logically it often matches
        behavior with `==` for basic equality unless specific mutability nuances apply.

        Args:
            a (Any): The first value to compare.
            b (Any): The second value to compare.

        Returns:
            bool: True if both values are the same object, False otherwise.
        """
        return a is b

if __name__ == '__main__':
    # Hard-coded sample values for testing
    checker = ValueChecker()