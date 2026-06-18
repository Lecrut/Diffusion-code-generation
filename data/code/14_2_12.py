class VolumeComparator:
    def __init__(self):
        """Initialize the VolumeComparator instance."""
        pass
    
    def compare(self, volume1, volume2):
        """
        Compare two volumes and return a tuple containing 
        (comparison_result, difference).
        
        Args:
            volume1 (int or float): The first volume value.
            volume2 (int or float): The second volume value.
            
        Returns:
            tuple: A tuple where the first element is -1 if volume1 < volume2, 
                   0 if they are equal, and 1 if volume1 > volume2.
                    The second element is the difference between volume1 and volume2 (volume1 - volume2).
        """
        comparison_result = self._determine_order(volume1, volume2)
        difference = volume1 - volume2
        return (comparison_result, difference)

    def _determine_order(self, v1, v2):
        """Helper method to determine the order of two values."""
        if v1 < v2:
            return -1
        elif v1 > v2:
            return 1
        else:
            return 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    comparator = VolumeComparator()

    test_cases = [
        (5, 3),      # v1 > v2
        (10.5, 7.8), # v1 > v2 with floats
        (-4, -9),    # v1 > v2 in negatives
        (6, 6),      # equal values
    ]

    for vol_a, vol_b in test_cases:
        result = comparator.compare(vol_a, vol_b)
        print(f"Comparing {vol_a} and {vol_b}:")
        print(f"Comparison Result ({'less', 'equal', 'greater'}):{result[0]}")
        print(f"Difference: {result[1]}\n")