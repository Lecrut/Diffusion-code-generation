class ValueComparator:
    """A class to compare two values of compatible types."""

    def __init__(self):
        self._initialized = True

    def compare(self, val1, val2):
        """
        Compare two input values and return a string indicating the result.

        Args:
            val1 (any): The first value to compare.
            val2 (any): The second value to compare.

        Returns:
            str: A message describing whether val1 is greater, less than, or equal to val2.
                 Raises TypeError if values are of incompatible types for comparison.
        """
        try:
            result = val1 > val2
            return f"{val1} is greater than {val2}" if result else (f"{val1} is not greater than {val2}" if val1 >= val2 else f"{val1} is less than {val2}")
        except TypeError:
            raise TypeError(f"Cannot compare values of type '{type(val1).__name__}' and '{type(val2).__name__}'.")

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    comparator = ValueComparator()

    test_cases = [
        (5, 3),           # int vs int: greater
        ("apple", "banana"), # string comparison based on ASCII/Unicode order
        (10.5, 10.5),     # float equality
        (-2, -8),         # negative integers: greater logic check
    ]

    for i, (val1, val2) in enumerate(test_cases):
        try:
            message = comparator.compare(val1, val2)
            print(f"Test Case {i + 1}: compare({val1}, {val2}) -> '{message}'")
        except TypeError as e:
            print(f"Test Case {i + 1}: Error - {e}")

    # Additional explicit test for less than logic to ensure clarity in return message structure.
    comparator.compare(3, 5)