class VolumeComparator:
    """A class to compare two volumes."""

    def compare(self, volume1, volume2):
        """
        Compares two volumes and returns a tuple containing 
        (comparison_result, difference).

        Args:
            volume1 (float or int): The first volume value.
            volume2 (float or int): The second volume value.

        Returns:
            tuple: A tuple where the first element is -1 if volume1 < volume2, 0 
                   if they are equal, and 1 otherwise; the second element is the 
                   difference between volume1 and volume2.
        """
        diff = volume1 - volume2
        
        if volume1 == volume2:
            result = "Equal"
            comparison_result = 0
        elif volume1 < volume2:
            result = f"{volume1} is less than {volume2}"
            comparison_result = -1
        else:
            result = f"{volume1} is greater than {volume2}"
            comparison_result = 1

        return (comparison_result, diff)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or arguments.
    vol_a = 50.5
    vol_b = 75.2
    
    comparator = VolumeComparator()
    result_tuple = comparator.compare(vol_a, vol_b)
    
    print(f"Comparison Result: {result_tuple[0]}")
    print(f"Difference ({vol_a} - {vol_b}): {result_tuple[1]}")