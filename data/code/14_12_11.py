class VolumeComparator:
    """A professional class designed to compare two volume measurements."""

    def __init__(self):
        self._comparison_count = 0

    def compare(self, volume1, volume2):
        """
        Compares two volume measurements and prints a descriptive string.

        Args:
            volume1 (float or int): The first volume measurement.
            volume2 (float or int): The second volume measurement.

        Prints:
            A message indicating which volume is greater, smaller, or if they are equal.
        """
        self._comparison_count += 1
        
        # Handle potential non-numeric inputs gracefully by attempting conversion
        try:
            val1 = float(volume1)
            val2 = float(volume2)
        except (ValueError, TypeError):
            print(f"Comparison failed for run #{self._comparison_count}: Invalid input types.")
            return

        if abs(val1 - val2) < 0.000001: # Floating point comparison with epsilon tolerance
            result = "equal"
        elif val1 > val2:
            result = f"{volume1} is greater than {volume2}"
        else:
            result = f"{volume2} is greater than {volume1}"

        print(f"Comparison #{self._comparison_count}: The volume of {result}.")

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    comparator = VolumeComparator()

    test_cases = [
        (50, 10),      # Case: First is greater
        (25.5, 30.7),  # Case: Second is greater
        (100, 100),    # Case: Equal integers
        (49.999999, 50.000001), # Case: Nearly equal floats
        ("invalid", "20"), # Case: Invalid input handling simulation logic would go here if expanded
    ]

    for v1, v2 in test_cases[:3]: # Running first three valid cases to demonstrate functionality
        comparator.compare(v1, v2)