class ValueComparator:
    """A class to compare two values of any type."""

    def __init__(self):
        pass

    @staticmethod
    def are_unequal(value1, value2) -> bool:
        """
        Compares two arguments and returns True if they are not equal.

        Args:
            value1 (any): The first value to compare.
            value2 (any): The second value to compare.

        Returns:
            bool: True if the values are unequal, False otherwise.
        """
        return value1 != value2

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or file access
    comp = ValueComparator()

    test_cases = [
        (5, 3),           # Integers: unequal -> True
        ("hello", "world"), # Strings: unequal -> True
        ([1, 2], [1, 2]),# Lists: equal -> False
        ((True,), (False,)),# Tuples: unequal -> True
    ]

    for i, (a, b) in enumerate(test_cases):
        result = comp.are_unequal(a, b)
        print(f"Comparison of {repr(a)} and {repr(b)} is {result}")