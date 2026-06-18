from typing import Any

class ValueChecker:
    """A utility class to check if two input values are identical."""

    def are_equal(self, a: Any, b: Any) -> bool:
        """
        Check if the two provided arguments are equal.

        This method compares both the type and the value of `a` and `b`.
        If they have different types or different values, it returns False.
        Otherwise, it returns True.

        Args:
            a (Any): The first input value to compare.
            b (Any): The second input value to compare.

        Returns:
            bool: True if `a` and `b` are identical in both type and value; False otherwise.
        """
        return a == b

if __name__ == '__main__':
    checker = ValueChecker()

    # Test cases with hard-coded sample values
    test_cases = [
        (10, 10),          # Same integers: expected True
        ("hello", "world"),# Different strings: expected False
        ([1, 2], [3, 4]), # Different lists: expected False
        ({'a': 1}, {'b': 2}), # Different dicts: expected False
        (True, True),      # Same booleans: expected True
    ]

    for i, inputs in enumerate(test_cases):
        a, b = inputs
        result = checker.are_equal(a, b)
        print(f"Test {i + 1}: are_equal({a}, {b}) -> {result}")