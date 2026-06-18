class VolumeComparator:
    """A class to compare two volume values."""

    def compare(self, volume1, volume2):
        """
        Compares two volumes and returns a tuple containing 
        the comparison result ('less', 'equal', or 'greater') 
        and the absolute difference between them.

        Args:
            volume1 (float/int/str representing number): The first volume value.
            volume2 (float/int/str representing number): The second volume value.

        Returns:
            tuple: A tuple of two elements - comparison result string and float difference.
        """
        # Convert inputs to floats for calculation, handling potential non-numeric strings if needed
        try:
            val1 = float(volume1)
            val2 = float(volume2)
        except (ValueError, TypeError):
            raise ValueError("Inputs must be convertible to numbers.")

        difference = abs(val1 - val2)

        if val1 < val2:
            comparison_result = "less"
        elif val1 > val2:
            comparison_result = "greater"
        else:
            comparison_result = "equal"

        return (comparison_result, difference)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    comp = VolumeComparator()
    
    # Sample 1: Comparing two integers
    result1 = comp.compare(50, 75)
    print(f"Comparing {result1[0]} with difference of {result1[1]:.2f}")

    # Sample 2: Comparing floats where they are equal
    result2 = comp.compare(3.14, 3.14)
    print(f"Comparing {result2[0]} with difference of {result2[1]:.2f}")

    # Sample 3: String inputs representing numbers
    result3 = comp.compare("10", "5")
    print(f"Comparing '{result3[0]}' (from strings) with difference of {result3[1]}")