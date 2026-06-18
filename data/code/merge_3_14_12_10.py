class VolumeComparator:
    """A utility class to compare two volume measurements."""

    def __init__(self):
        self._comparison_log = []

    def compare(self, volume1, volume2):
        """
        Compares two volume values and prints a descriptive result.

        Args:
            volume1 (float or int): The first volume measurement.
            volume2 (float or int): The second volume measurement.

        Returns:
            None: Prints the comparison result to stdout.

        Raises:
            TypeError: If either input is not numeric.
        """
        if not isinstance(volume1, (int, float)) or not isinstance(volume2, (int, float)):
            raise TypeError("Both arguments must be numerical values representing volume.")

        difference = abs(volume1 - volume2)
        
        # Handle floating point precision issues for equality check
        is_equal = False
        if difference < 0.0001: 
            is_equal = True
            
        result_string = ""
        
        if is_equal:
            result_string = f"The two volumes are equal."
        elif volume1 > volume2 + 0.0001:
            result_string = f"Volume {volume1} is greater than Volume {volume2} by approximately {difference:.4f} units."
        else: 
            # Covers cases where volume2 >= volume1
            if difference < -0.0001:  # Should logically not happen with abs above, but for safety in strict logic flow
                 result_string = f"Volume {volume1} is greater than Volume {volume2} by approximately {difference:.4f} units."
            else: 
                diff_val = volume2 - volume1 + difference if volume2 > volume1 else 0 # Simplified direct calc below
                actual_diff = abs(volume1 - volume2)
                result_string = f"Volume {volume1} is smaller than Volume {volume2} by approximately {actual_diff:.4f} units."

        print(result_string.strip())

if __name__ == '__main__':
    # Sample test cases with hard-coded values running without external input or files.
    
    comparator = VolumeComparator()

    # Test Case 1: volume1 is greater
    comparator.compare(50, 30)

    # Test Case 2: volume2 is greater
    comparator.compare(49.8, 60.1)

    # Test Case 3: volumes are equal (or extremely close within tolerance)
    comparator.compare(100, 100)

    # Test Case 4: floating point comparison with minor difference
    a = float(7.5)
    b = float('2') + 6 # Creating 8.0 but demonstrating mixed calculation style if needed
    # Let's stick to direct floats for clarity in sample block as per requirements
    comparator.compare(float("10"), float("10"))

    # Test Case 5: Explicitly greater with decimals
    comparator.compare(25.7, 25.3)