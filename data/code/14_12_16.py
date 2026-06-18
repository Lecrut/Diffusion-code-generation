import sys

class VolumeComparator:
    """A professional utility class for comparing volume measurements."""

    def compare(self, volume1, volume2):
        """
        Compares two numeric volume values and prints a descriptive result.

        Args:
            volume1 (float or int): The first volume measurement.
            volume2 (float or int): The second volume measurement.

        Prints to stdout one of the following strings based on comparison:
            - "Volume 1 is greater than Volume 2" if volume1 > volume2
            - "Volume 2 is greater than Volume 1" if volume2 > volume1
            - "Both volumes are equal" if volume1 == volume2

        Raises:
            TypeError: If either input is not a number.
        """
        # Validate inputs to ensure they are numeric
        if not isinstance(volume1, (int, float)) or not isinstance(volume2, (int, float)):
            raise TypeError("Both arguments must be numbers.")

        comparison_result = volume1 > volume2
        
        if comparison_result:
            print(f"Volume 1 is greater than Volume 2")
        elif volume2 > volume1:
            print(f"Volume 2 is greater than Volume 1")
        else:
            print("Both volumes are equal")

if __name__ == '__main__':
    # Hard-coded sample values for demonstration; no user input required.
    comparator = VolumeComparator()

    test_cases = [
        (50, 25),      # Case A: First volume is larger
        (10, 30),      # Case B: Second volume is larger
        (75.5, 75.5),  # Case C: Volumes are equal
    ]

    for v1, v2 in test_cases:
        comparator.compare(v1, v2)