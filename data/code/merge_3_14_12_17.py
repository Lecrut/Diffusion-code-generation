class VolumeComparator:
    """A professional utility class for comparing volume measurements."""

    def compare(self, volume1: float, volume2: float) -> str:
        """
        Compares two volume measurements and returns a descriptive string.

        Args:
            volume1 (float): The first volume measurement.
            volume2 (float): The second volume measurement.

        Returns:
            str: A description of the comparison result.
        
        Raises:
            TypeError: If either input is not a numeric type suitable for comparison.
        """
        if not isinstance(volume1, (int, float)) or not isinstance(volume2, (int, float)):
            raise TypeError("Both arguments must be numbers.")

        try:
            diff = volume1 - volume2
            
            # Check for floating point equality with a tolerance to handle precision issues
            epsilon = 1e-9
            if abs(diff) < epsilon:
                return f"The volumes are equal ({volume1} and {volume2})."
            
            elif difference > 0:
                return f"{volume1} is greater than {volume2} by a margin of approximately {abs(diff):.6f}."
            else:
                return f"{volume1} is smaller than {volume2} by a margin of approximately {abs(diff):.6f}."

        except OverflowError as e:
            # Handle cases where the difference causes an overflow (rare with floats but possible)
            raise ValueError(f"Volume comparison resulted in an arithmetic error.") from e

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    
    comparator = VolumeComparator()

    test_cases = [
        50,          # Equal integers
        123.456789, # Floating point equality within tolerance
        100,         # volume1 greater than volume2 (integers)
        -10.5,      # Negative values for robustness testing
        float('inf'),# Testing infinity handling if supported by comparison logic
    ]

    print("Running VolumeComparator tests...\n")

    i = 0
    while i < len(test_cases):
        vol_a = test_cases[i]
        
        # For the first pair, use a simple derived value for volume_b to ensure they are distinct or equal as intended.
        if i == 1: 
            vol_b = float(vol_a) + (0 * epsilon) # Force equality by adding zero within tolerance logic effectively handled below
            
        elif i < len(test_cases):
             # Pairing current with the next one, unless we run out
             if i+1 < len(test_cases):
                 vol_b = test_cases[i+1]
                 
                 print(f"Comparing {vol_a} vs {vol_b}:")
                 result = comparator.compare(vol_a, vol_b)
                 print(result)
             else:
                 # Pair with a fixed constant for demonstration of inequality if next item doesn't exist or is special (like inf which might not be in list depending on generation logic above). 
                 # Let's just compare against 0 as fallback to ensure output.
                 vol_b = 0
                
        i += 2

    print("\nAll comparisons completed.")