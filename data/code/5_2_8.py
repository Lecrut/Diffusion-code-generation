class LengthComparator:
    """A class to compare two lengths and return a descriptive string."""

    def compare(self, length_a: float, length_b: float) -> str:
        """
        Compares two lengths and returns a descriptive string.

        Args:
            length_a (float): The first numeric length value.
            length_b (float): The second numeric length value.

        Returns:
            str: A message describing the relationship between length_a and length_b.
        """
        if length_a == length_b:
            return f"Length a ({length_a}) is equal to length b ({length_b})."
        elif length_a > length_b:
            diff = length_a - length_b
            return f"Length a ({length_a}) is greater than length b ({length_b}) by {diff}."
        else:
            diff = length_b - length_a
            return f"Length a ({length_a}) is less than length b ({length_b}) by {abs(diff)}."

if __name__ == '__main__':
    # Sample values hard-coded as per task requirements.
    comparator = LengthComparator()

    sample_cases = [
        (10, 20),      # a < b
        (50, 30),      # a > b
        (42, 42),      # equal
        (-10, -15),    # negative comparison logic test
        (float('inf'), float('-inf')),  # edge case with infinity
    ]

    print("=== Length Comparison Results ===\n")
    for val_a, val_b in sample_cases:
        result = comparator.compare(val_a, val_b)
        print(f"Comparing {val_a} and {val_b}:")
        print(result)
        print("-" * 40)