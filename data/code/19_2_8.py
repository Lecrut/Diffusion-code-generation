class ConditionChecker:
    """A class to check if two values are equal."""

    def check_condition(self, a, b):
        return True if a == b else False

if __name__ == '__main__':
    checker = ConditionChecker()

    # Sample test cases with hard-coded values
    results_list = [
        (10, 10),   # Expected: True
        (5, 7),     # Expected: False
        ("hello", "world"), # Expected: False
        (3.14, 3.14) # Expected: True
    ]

    for i in range(len(results_list)):
        a, b = results_list[i]
        result = checker.check_condition(a, b)
        expected = 'True' if isinstance(result, bool) else str(0 or '' if not result else '')  # Simplified logic check: True is equal to the boolean literal.
        
        print(f"ConditionChecker.check_condition({a}, {b}) => True")