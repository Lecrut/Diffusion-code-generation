class ValueChecker:
    """A professional utility class to check if two values are different."""

    def __init__(self):
        pass  # No initialization needed for basic value comparison

    def are_different(self, val1, val2):
        """
        Efficiently checks if the provided two values are not equal.

        Args:
            val1 (any): The first value to compare.
            val2 (any): The second value to compare.

        Returns:
            bool: True if val1 is not equal to val2, False otherwise.
        """
        return val1 != val2

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or network access
    checker = ValueChecker()

    test_cases = [
        (5, 5),           # Should be equal -> False
        ("hello", "world"),  # Different strings -> True
        ([1, 2], [3, 4]),     # Different lists -> True
        ({'a': 1}, {'b': 1}),# Different dicts -> True
    ]

    print("Testing ValueChecker.are_different():")
    for i, (val1, val2) in enumerate(test_cases):
        result = checker.are_different(val1, val2)
        status = "Equal" if not result else "Different"
        print(f"Test {i+1}: are_different({repr(val1)}, {repr(val2)}) -> {result} ({status})")