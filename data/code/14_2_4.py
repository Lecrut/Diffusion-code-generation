class VolumeComparator:
    """A class to compare two volumes."""

    def __init__(self):
        self.comparisons = []

    def compare(self, volume1, volume2) -> tuple:
        """
        Compares two volumes.

        Args:
            volume1 (float or int): The first volume value.
            volume2 (float or int): The second volume value.

        Returns:
            tuple: A tuple containing the comparison result ('<', '>', '=') and 
                   the absolute difference between the two volumes.
        """
        diff = abs(volume1 - volume2)
        
        if volume1 < volume2:
            return ("<", diff)
        elif volume1 > volume2:
            return (">", diff)
        else:
            return ("=", diff)

if __name__ == '__main__':
    # Sample values hard-coded for testing purposes.
    vol_a = 50.7
    vol_b = 43.2

    comparator = VolumeComparator()
    
    result, difference = comparator.compare(vol_a, vol_b)
    
    print(f"Comparing {vol_a} and {vol_b}")
    print(f"Result: {result[0]}")
    print(f"Difference: {difference}")