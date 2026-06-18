class ValueComparator:
    """A class that compares two values and returns a descriptive string."""

    def compare(self, val1, val2):
        """
        Compares two input values of any comparable type (numbers, strings).

        Args:
            val1: The first value to compare.
            val2: The second value to compare.

        Returns:
            A string indicating which value is greater, less, or if they are equal.
        """
        try:
            result = val1 > val2
            return "val1" if result else ("val2" if not (result := val1 < val2) else f"{val1} and {val2}")
        except TypeError:
            raise TypeError("Values must be of comparable types.")

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    comparator = ValueComparator()

    test_cases = [
        (10, 5),           # val1 > val2
        ("apple", "banana"), # val1 < val2
        (3.14, 3.14),     # Equal values
        (-7, -3),          # val1 < val2
    ]

    for v1, v2 in test_cases:
        output = comparator.compare(v1, v2)
        print(f"Comparing {v1} and {v2}: {output}")