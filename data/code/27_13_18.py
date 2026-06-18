class ValueChecker:
    """A professional utility class to check inequality between two values."""

    def __init__(self):
        """Initialize the ValueChecker instance with no dependencies."""
        pass

    def are_different(self, val1, val2) -> bool:
        """
        Check if the provided two values are not equal.

        This method uses Python's native identity and equality operators
        to handle various data types efficiently without overhead.

        Args:
            val1 (any): The first value to compare.
            val2 (any): The second value to compare.

        Returns:
            bool: True if the values are not equal, False otherwise.
        """
        return val1 != val2

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    checker = ValueChecker()

    test_cases = [
        (5, 5),           # Should be False: equal integers
        ("hello", "world"),  # Should be True: different strings
        (3.14, 2.71),     # Should be True: different floats
        ([1, 2], [1, 2]),   # Should be False: identical lists
        ({'a': 1}, {'b': 1}),    # Should be True: different dicts
        (None, None),      # Should be False: both are None
        ("", ""),          # Should be False: empty strings equal
        (True, False),     # Should be True: boolean values differ
    ]

    print("ValueChecker Inequality Tests:")
    for i, (val1, val2) in enumerate(test_cases, 1):
        result = checker.are_different(val1, val2)
        status = "Different" if result else "Same"
        print(f"Test {i}: {repr(val1)} vs {repr(val2)} -> Are different: {result} ({status})")