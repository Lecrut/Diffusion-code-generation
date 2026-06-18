class ValueComparator:
    """A class that encapsulates logic for comparing two input values."""

    def compare(self, val1, val2):
        """
        Compares two values and returns a string indicating their relationship.

        Args:
            val1 (any comparable type): The first value to compare.
            val2 (any comparable type): The second value to compare.

        Returns:
            str: A message describing the comparison result ('val1 is greater', 
                 'val2 is greater', or 'values are equal').
        """
        try:
            if val1 > val2:
                return f"{type(val1).__name__} value '{val1}' is greater than {type(val2).__name__} value '{val2}'"
            elif val2 > val1:
                return f"{type(val2).__name__} value '{val2}' is greater than {type(val1).__name__} value '{val1}'"
            else:
                return f"'{val1}' and '{val2}' are equal."
        except TypeError as e:
            raise TypeError(f"Incompatible types for comparison: cannot compare {type(val1)} with {type(val2)}.") from e

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    comparator = ValueComparator()

    test_cases = [
        (5, 3),
        ("apple", "banana"),
        (10.5, 10.5),
        (-2, -8),
    ]

    for val1, val2 in test_cases:
        result = comparator.compare(val1, val2)
        print(result)