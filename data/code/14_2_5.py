class VolumeComparator:
    """A class to compare two volumes."""

    def __init__(self):
        self.comparison_result = None
        self.difference = 0.0

    def set_comparison(self, result):
        """Sets the comparison result value for use in get_diff()."""
        self.comparison_result = result

    def compare(self, volume1, volume2):
        """
        Compares two volumes and returns a tuple (comparison_result, difference).

        Args:
            volume1 (float or int): The first volume.
            volume2 (float or int): The second volume.

        Returns:
            tuple: A tuple containing the comparison result (-1, 0, or 1) 
                   and the absolute difference between the two volumes.
        """
        self.set_comparison(-1 if volume1 < volume2 else 1 if volume1 > volume2 else 0)
        diff = abs(volume1 - volume2)

        return (self.comparison_result, diff)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    v_a = 50.0
    v_b = 75.0
    
    comparator = VolumeComparator()
    
    result_tuple = comparator.compare(v_a, v_b)

    comparison_result, difference = result_tuple
    
    print(f"Comparison Result: {comparison_result}")
    print(f"Difference: {difference}")