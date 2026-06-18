class ConditionChecker:
    def check_condition(self, a, b):
        """
        Checks if two values 'a' and 'b' are equal.

        Args:
            a (any): The first value to compare.
            b (any): The second value to compare.

        Returns:
            bool: True if a is equal to b, False otherwise.
        """
        return a == b

if __name__ == '__main__':
    checker = ConditionChecker()

    # Sample test cases with hard-coded values
    print(checker.check_condition(5, 5))      # Expected: True
    print(checker.check_condition("hello", "world"))  # Expected: False
    print(checker.check_condition([1, 2], [1, 2]))       # Expected: True
    print(checker.check_condition(True, False))     # Expected: False