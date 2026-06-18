import sys

class VolumeComparator:
    """
    A class designed to compare two volume measurements efficiently.
    
    Attributes:
        None
    
    Methods:
        compare(volume1, volume2): Compares two volumes and prints a descriptive result.
        
    Usage Example:
        >>> comp = VolumeComparator()
        >>> comp.compare(50, 75)
        "Volume 75 is greater than Volume 50."
    """

    def compare(self, volume1: float, volume2: float) -> None:
        """
        Compares two volume measurements and prints a descriptive string.
        
        Args:
            volume1 (float): The first volume measurement to be compared.
            volume2 (float): The second volume measurement to be compared.
            
        Returns:
            None
            
        Raises:
            TypeError: If either input is not a numeric type.
        """
        if not isinstance(volume1, (int, float)) or not isinstance(volume2, (int, float)):
            raise TypeError("Both arguments must be numbers.")

        diff = volume2 - volume1
        
        # Use absolute difference to determine equality without floating-point epsilon issues for simple cases,
        # but given the requirement for "professional" handling of potential floats, we use a small tolerance.
        EPSILON = 1e-9
        
        if abs(diff) < EPSILON:
            print(f"The volumes are equal.")
        elif diff > 0:
            print(f"{volume2} is greater than {volume1}.")
        else:
            print(f"{volume1} is greater than {volume2}.")

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    comparator = VolumeComparator()

    test_cases = [
        (50, 75),      # Case: volume2 > volume1
        (3.5, 3.5),    # Case: equal volumes
        (100, 98.4),   # Case: volume1 > volume2 with decimals
        (-10, -20),    # Case: negative numbers where volume1 is greater
    ]

    for v1, v2 in test_cases:
        comparator.compare(v1, v2)