class VolumeComparator:
    """A professional class to compare two volume measurements."""
    
    def __init__(self):
        pass
    
    def compare(self, volume1, volume2):
        """
        Compares two volume measurements and prints a descriptive result.
        
        Args:
            volume1 (float or int): The first volume measurement.
            volume2 (float or int): The second volume measurement.
            
        Returns:
            None
            
        Prints a string indicating which volume is greater, smaller, or if they are equal.
        Handles floating point comparison with an epsilon tolerance for precision.
        """
        # Use a small epsilon value to handle potential floating-point arithmetic inaccuracies
        EPSILON = 1e-9
        
        diff = abs(volume1 - volume2)
        
        if diff < EPSILON:
            print(f"The volumes are equal ({volume1} and {volume2}).")
        elif volume1 > volume2 + EPSILON:
            print(f"Volume 1 is greater than Volume 2. Difference: {abs(volume1 - volume2):.6f}")
        else: # volume2 > volume1 + EPSILON
            print(f"Volume 2 is greater than Volume 1. Difference: {abs(volume2 - volume1):.6f}")

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    comparator = VolumeComparator()

    # Sample Test Case 1: Integers with different magnitudes
    result_1 = comparator.compare(50, 75)
    
    # Sample Test Case 2: Floating-point numbers close in value (near equal within tolerance)
    val_a = 3.49999999
    val_b = 3.50000001
    result_2 = comparator.compare(val_a, val_b)

    # Sample Test Case 3: Zero vs Negative volume (assuming volumes can be negative in context like debt or pressure)
    result_3 = comparator.compare(-10, -5)

    # Sample Test Case 4: Very large difference to ensure efficiency is not impacted by value size
    result_4 = comparator.compare(1e-20, 1e+20)
    
    print("All comparisons completed successfully.")