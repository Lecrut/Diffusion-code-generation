class ConditionChecker:
    """A class to check if two values are equal."""

    def check_condition(self, a, b):
        """Returns True if a is equal to b, False otherwise.
        
        Args:
            a: The first value to compare.
            b: The second value to compare.
            
        Returns:
            bool: True if a == b, else False.
        """
        return a == b

if __name__ == '__main__':
    checker = ConditionChecker()

    # Test cases with hard-coded sample values
    test_cases = [
        (5, 5),      # Should be True
        ("hello", "world"),  # Should be False
        (3.14, 3.14),     # Should be True
        ([1, 2], [1, 2]), # Should be True
    ]

    for val_a, val_b in test_cases:
        result = checker.check_condition(val_a, val_b)
        print(f"check_condition({val_a!r}, {val_b!r}) returned {result}")