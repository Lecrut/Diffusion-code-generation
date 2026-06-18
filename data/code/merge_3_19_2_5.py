class ConditionChecker:
    """A class that checks if two values are equal."""

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
    print(checker.check_condition(5, 5))      # Expected: True
    print(checker.check_condition("hello", "world"))   # Expected: False
    print(checker.check_condition(True, True))     # Expected: True
    print(checker.check_condition([], []))          # Expected: True