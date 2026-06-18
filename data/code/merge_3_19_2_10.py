class ConditionChecker:
    """A simple class to check equality between two values."""

    def check_condition(self, a, b):
        """Returns True if 'a' is equal to 'b', False otherwise.

        Args:
            a (Any): The first value to compare.
            b (Any): The second value to compare.

        Returns:
            bool: True if values are equal, False otherwise.
        """
        return a == b

if __name__ == '__main__':
    checker = ConditionChecker()

    # Sample test cases with hard-coded values
    tests = [
        (5, 5),       # Should be True
        ("hello", "world"),  # Should be False
        (10.5, 10.5),# Should be True
        ([], []),     # Should be True
        ({}, {}),     # Note: Dicts compare equal if keys/values are same structure
    ]

    for a, b in tests:
        result = checker.check_condition(a, b)
        print(f"check_condition({a!r}, {b!r}) -> {result}")