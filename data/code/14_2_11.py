class VolumeComparator:
    def compare(self, volume1, volume2):
        """
        Compare two volumes and return a tuple with comparison result and difference.
        
        Args:
            volume1 (float or int): First volume value.
            volume2 (float or int): Second volume value.
            
        Returns:
            tuple: A tuple containing the comparison status ('less', 'equal', or 'greater')
                   and the numerical difference between the two volumes.
        
        Example:
            >>> comparator = VolumeComparator()
            >>> result, diff = comparator.compare(10, 20)
            # Returns: ('less', -10.0)
        """
        if volume1 < volume2:
            return ("less", volume1 - volume2)
        elif volume1 > volume2:
            return ("greater", volume1 - volume2)
        else:
            return ("equal", 0.0)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    comparator = VolumeComparator()

    test_cases = [
        (5, 10),      # Less case
        (20, 15),     # Greater case
        (7.5, 7.5),   # Equal float case
        (-3, -3),     # Negative equal case
        (42, 9)       # Large difference case
    ]

    print("Volume Comparison Results:")
    for vol1, vol2 in test_cases:
        result, diff = comparator.compare(vol1, vol2)
        if result == "less":
            status_str = f"{vol1} is less than {vol2}"
        elif result == "greater":
            status_str = f"{vol1} is greater than {vol2}"
        else:
            status_str = f"{vol1} equals {vol2}"
        
        print(f"Comparison of {vol1} and {vol2}:")
        print(f"  Status: {status_str}")
        print(f"  Difference ({vol1} - {vol2}): {diff}\n")