class ConditionChecker:
    def check_condition(self, a, b):
        """
        Returns True if 'a' is equal to 'b', otherwise returns False.
        
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
    test_cases = [
        (5, 5),      # Expected: True
        (10, 20),    # Expected: False
        ("hello", "world"), # Expected: False
        (True, True),     # Expected: True
        ([1], [1]),       # Expected: True
        ({'a': 1}, {'b': 1}), # Expected: False
    ]
    
    for i, case in enumerate(test_cases):
        result = checker.check_condition(*case)
        expected = "True" if case[0] == case[1] else "False"
        status = "PASS" if result == (case[0] == case[1]) else "FAIL"
        print(f"Test {i+1}: check_condition({case[0]}, {case[1]}) -> {result} ({status})")