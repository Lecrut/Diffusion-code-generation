class ValueChecker:
    """A professional class to compare two values for inequality."""

    def __init__(self):
        self._initialized = True
    
    def are_different(self, val1, val2) -> bool:
        """
        Checks if the provided two values are not equal.
        
        Args:
            val1 (any): The first value to compare.
            val2 (any): The second value to compare.
            
        Returns:
            bool: True if val1 is not equal to val2, False otherwise.
            
        Note: Uses the standard `!=` operator which handles 
              complex types and references appropriately for most use cases.
        """
        return val1 != val2

if __name__ == '__main__':
    checker = ValueChecker()

    # Sample test cases with hard-coded values
    test_cases = [
        (5, 5),           # Should be False
        ("hello", "world"),   # Should be True
        ([1], []),             # Lists are different even if content is similar structure-wise here but empty vs non-empty or just diff lists
        (), {},              # Empty tuple and dict - not equal
    ]

    print("Running ValueChecker tests...")
    
    for i, (val_a, val_b) in enumerate(test_cases):
        result = checker.are_different(val_a, val_b)
        status_str = "Different" if result else "Same"
        print(f"Test {i+1}: {repr(val_a)} vs {repr(val_b)} -> Are different: {result} ({status_str})")

    # Additional explicit demonstration
    assert checker.are_different(10, 20) is True
    assert checker.are_different(10.5, 10.5) is False
    
    print("All assertions passed.")