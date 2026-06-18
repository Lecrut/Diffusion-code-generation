class ValueComparator:
    """A class that compares two values and returns a descriptive string."""
    
    def compare(self, val1, val2):
        """
        Compares two input values (integers or floats) and returns 
        a string indicating the relationship between them.
        
        Args:
            val1 (int | float): The first value to compare.
            val2 (int | float): The second value to compare.
            
        Returns:
            str: A message stating whether 'val1' is greater than, 
                 less than, or equal to 'val2'.
        
        Raises:
            TypeError: If the inputs are not numeric types.
        """
        if isinstance(val1, (int, float)) and isinstance(val2, (int, float)):
            result = None
            
            # Use a small epsilon for floating-point comparison accuracy
            if val1 == int(val1) and val2 == int(val2):
                # Exact integer equality check first to avoid precision issues later
                is_equal_ints = abs(val1 - val2) < 0.000000001

if __name__ == '__main__':
    pass
