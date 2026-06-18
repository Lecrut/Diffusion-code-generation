class ValueComparator:
    """A class that compares two values of any comparable type."""

    def compare(self, val1, val2):
        """
        Compares two input values and returns a string indicating their relationship.

        Args:
            val1 (any): The first value to compare.
            val2 (any): The second value to compare.

        Returns:
            str: A message describing the comparison result ('val1 is greater', 
                 'val2 is greater', or 'values are equal'). Raises TypeError if types differ,
                 as Python's default comparison behavior handles type mismatches appropriately.
        """
        try:
            # Attempt to compare using standard operators; this implicitly checks for comparable types
            result = val1 > val2
            return "val1 is greater" if result else ("values are equal" if not (result or val1 < val2) else "val2 is greater")
        except TypeError:
            # If comparison fails due to incompatible types, raise a descriptive error
            raise TypeError(f"Incompatible types for comparison. Type of val1: {type(val1)}, Type of val2: {type(val2)}")

if __name__ == '__main__':
    # Hard-coded sample values demonstrating various scenarios
    comparator = ValueComparator()

    test_cases = [
        (5, 3),           # Integer comparison
        ("apple", "banana"),  # String comparison
        (10.5, 10.5),     # Float equality
        (-2, -8),         # Negative integer comparison
        ([1], [1]),       # List equality
    ]

    for val1, val2 in test_cases:
        result = comparator.compare(val1, val2)
        print(f"Comparing {val1} and {val2}: '{result}'")