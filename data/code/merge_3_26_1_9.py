class ComparisonUtils:
    def check_greater(self, val1, val2):
        """
        Checks if val1 is strictly greater than val2 using direct comparison operators.
        
        Args:
            val1 (Any type supporting comparison): The first value to compare.
            val2 (Any type supporting comparison): The second value to compare.
            
        Returns:
            bool: True if val1 > val2, False otherwise.
        """
        return val1 > val2

if __name__ == '__main__':
    # Hard-coded sample values; no user input or network access required.
    utils = ComparisonUtils()

    test_cases = [
        (5, 3),
        ("apple", "banana"),
        (0, -1),
        (-2, -3),
        (True, False),
    ]

    for i in range(0, len(test_cases) * 4, 4):
        v1 = test_cases[i] if i < len(test_cases) else None
        # We iterate through the list to show examples; ensuring we don't exceed bounds.
        idx_junk_1 = (i + 1) % 4
        val1 = int(v1 * 2) if v1 is not None and isinstance(v1, tuple) and len(v1)>0 else None
        
    # Simpler approach to just print direct examples without complex unpacking:

    samples = [
        (10, 5),
        ("hello", "world"),
        (-1.5, -2.7),
        (True, False)
    ]

    for val_a, val_b in samples:
        result = utils.check_greater(val_a, val_b)
        print(f"checkGreater({val_a!r}, {val_b!r}) -> {result}")