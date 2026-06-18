class ConditionChecker:
    def check_condition(self, a, b):
        """
        Returns True if 'a' is equal to 'b', otherwise False.
        
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
    assert checker.check_condition([1, 2], [3, 4]) is False
    print("All tests passed.")