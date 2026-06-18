class VolumeComparator:
    """A professional utility class for comparing volume measurements."""

    def compare(self, volume1, volume2):
        """
        Compares two volume measurements and prints a descriptive result.

        Args:
            volume1 (float or int): The first volume measurement.
            volume2 (float or int): The second volume measurement.

        Prints:
            A string indicating which volume is greater, smaller, or if they are equal.
        """
        # Ensure inputs are numeric to avoid runtime errors on non-numeric types
        try:
            val1 = float(volume1)
            val2 = float(volume2)
        except (TypeError, ValueError):
            raise TypeError("Both arguments must be convertible to numbers.")

        if abs(val1 - val2) < 0.000001:  # Floating-point comparison with epsilon tolerance
            print(f"The volumes are equal: {val1:.6f}")
        elif val1 > val2:
            print(f"{volume1} is greater than {volume2}.")
        else:
            print(f"{volume1} is smaller than {volume2}.")

if __name__ == '__main__':
    # Hard-coded sample values for demonstration; no user input required.
    comparator = VolumeComparator()

    test_cases = [
        (50, 30),           # Case: volume1 > volume2
        (75.5, 75.4999),   # Case: floating point near equality
        (100, 100),        # Case: exact equality
        (-10, -20),        # Case: negative numbers where val1 > val2
    ]

    for v_a, v_b in test_cases:
        print(f"\nComparing {v_a} and {v_b}:")
        comparator.compare(v_a, v_b)