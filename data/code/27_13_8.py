class ValueChecker:
    def __init__(self):
        """Initialize the ValueChecker instance."""
        pass
    
    def are_different(self, val1, val2):
        """
        Check if two provided values are not equal.
        
        Args:
            val1 (any): The first value to compare.
            val2 (any): The second value to compare.
            
        Returns:
            bool: True if the values are different, False otherwise.
        """
        return val1 != val2

if __name__ == '__main__':
    checker = ValueChecker()
    
    # Sample test cases with hard-coded values
    
    # Test 1: Integers that are equal
    result1 = checker.are_different(5, 5)
    
    # Test 2: Strings that differ by case but same content value (handled as different strings in Python)
    # Note: 'Hello' and 'hello' are not equal because they have different ASCII values.
    result3 = checker.are_different('A', 'a')

    print(f"Test 1 (5 vs 5): {result1}")
    print(f"Test 2 ('A' vs 'a'): {result3}")