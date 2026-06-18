class ValueChecker:
    """A professional class designed to check inequality between two values efficiently."""

    def __init__(self):
        pass

    def are_different(self, val1, val2) -> bool:
        """
        Checks if the provided two values are not equal.
        
        This method uses Python's built-in comparison operators which handle 
        all data types (integers, floats, strings, objects) appropriately and efficiently.
        
        Args:
            val1 (any): The first value to compare.
            val2 (any): The second value to compare.
            
        Returns:
            bool: True if val1 is not equal to val2, False otherwise.
        """
        return val1 != val2

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    checker = ValueChecker()

    test_cases = [
        (5, 5),           # Should be False
        ("hello", "world"), # Should be True
        (3.14, 2.71),   # Should be True
        ([], []),         # Should be False
        ({}, {}),         # Should be False
    ]

    for val1, val2 in test_cases:
        result = checker.are_different(val1, val2)
        print(f"are_different({val1!r}, {val2!r}) = {result}")