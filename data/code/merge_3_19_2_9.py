class ConditionChecker:
    """A class that provides methods to check conditions between two values."""

    def check_condition(self, a, b):
        """Returns True if 'a' is equal to 'b', and False otherwise.

        Args:
            a (any): The first value to compare.
            b (any): The second value to compare.

        Returns:
            bool: True if values are equal, False otherwise.
        """
        return a == b

if __name__ == '__main__':
    checker = ConditionChecker()

    # Sample test cases with hard-coded values
    assert checker.check_condition(5, 5) is True
    assert checker.check_condition("hello", "world") is False
    assert checker.check_condition(True, True) is True
    assert checker.check_condition([], []) is True

    print("All condition checks passed.")