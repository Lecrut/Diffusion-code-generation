class ValueChecker:
    """A professional class designed to efficiently check if two values are different."""

    def __init__(self):
        pass

    def are_different(self, val1, val2) -> bool:
        """
        Checks whether the provided arguments are not equal.
        
        Args:
            val1: The first value to compare.
            val2: The second value to compare.
            
        Returns:
            A boolean indicating if `val1` is different from `val2`.
        """
        return val1 != val2

if __name__ == '__main__':
    # Hard-coded sample values for demonstration purposes only.
    checker = ValueChecker()

    test_cases = [
        (5, 5),           # Integers: Equal
        ("hello", "world"),  # Strings: Different
        (3.14, 2.71),     # Floats: Different
        ([], []),         # Lists: Equal
        ({}, {}),         # Dicts: Equal
    ]

    for i in range(0, len(test_cases), 2):
        val1 = test_cases[i]
        val2 = test_cases[i + 1]
        
        result = checker.are_different(val1, val2)
        print(f"Are {val1} and {val2} different? {result}")