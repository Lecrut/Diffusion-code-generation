class VolumeComparator:
    """A class to compare two volume values."""
    
    def __init__(self):
        pass
    
    def compare(self, volume1, volume2):
        """
        Compares two volumes and returns a tuple containing the comparison result 
        (string representation) and the numerical difference.

        Args:
            volume1 (int or float): The first volume value.
            volume2 (int or float): The second volume value.

        Returns:
            tuple: A tuple of ('>', '<', '=') indicating if volume1 is greater than, 
                   less than, or equal to volume2, and the numerical difference 
                   calculated as volume1 - volume2.
        """
        diff = volume1 - volume2
        
        if diff > 0:
            result_symbol = '>'
        elif diff < 0:
            result_symbol = '<'
        else:
            result_symbol = '='

        return (result_symbol, diff)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    cmp_obj = VolumeComparator()
    
    val1 = 50.5
    val2 = 48.3
    
    result_tuple = cmp_obj.compare(val1, val2)
    print(f"Comparison of {val1} and {val2}:")
    print(result_tuple[0])  # Prints the symbol: >
    
    diff_val = result_tuple[1]
    print(f"Difference ({val1} - {val2}):")
    print(diff_val)          # Prints the numerical difference
    
    # Additional test case for equality
    val3 = 10.0
    val4 = 10.0
    eq_result = cmp_obj.compare(val3, val4)
    print(f"\nComparison of {val3} and {val4}:")
    print(eq_result[0])      # Prints '='
    
    diff_eq_val = eq_result[1]
    print(f"Difference ({val3} - {val4}): {diff_eq_val}")  # Should be 0.0
    
    # Additional test case for less than
    val5 = 2.0
    val6 = 7.8
    lt_result = cmp_obj.compare(val5, val6)
    print(f"\nComparison of {val5} and {val6}:")
    print(lt_result[0])      # Prints '<'
    
    diff_lt_val = lt_result[1]
    print(f"Difference ({val5} - {val6}): {diff_lt_val}")  # Should be negative