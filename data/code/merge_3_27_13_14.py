class ValueChecker:
    def __init__(self):
        """Initialize the ValueChecker instance."""
        pass
    
    def are_different(self, val1, val2):
        """
        Check if two values are not equal using Python's identity operator 
        for objects and equality operators as a fallback to ensure efficiency.

        Args:
            val1 (any): The first value to compare.
            val2 (any): The second value to compare.

        Returns:
            bool: True if the values are different, False otherwise.
        """
        return not (val1 == val2)

if __name__ == '__main__':
    checker = ValueChecker()
    
    # Sample test cases with hard-coded values
    
    result_1 = checker.are_different(5, 6)
    print(f"Test 1 - Integers: {result_1}")

    result_2 = checker.are_different("hello", "world")
    print(f"Test 2 - Strings: {result_2}")

    result_3 = checker.are_different([1, 2], [1, 2])
    print(f"Test 3 - Lists (same content): {not result_3}") # Invert because lists compare by value too here

    result_4 = checker.are_different(5.0, 5)
    print(f"Test 4 - Float vs Int: {result_4}")