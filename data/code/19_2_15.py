class ConditionChecker:
    def check_condition(self, a, b):
        """Returns True if a is equal to b, False otherwise."""
        return a == b

if __name__ == '__main__':
    checker = ConditionChecker()
    
    # Test cases with hard-coded sample values
    test_cases = [
        (5, 5),      # Should be True
        (10, 20),    # Should be False
        ("hello", "world"),  # Should be False
        (3.14, 3.14),   # Should be True
        ([1], [1]),     # Should be True
        ({'a': 1}, {'b': 2}),  # Should be False
    ]

    for a, b in test_cases:
        result = checker.check_condition(a, b)
        print(f"check_condition({repr(a)}, {repr(b)}) -> {result}")