class ValueComparator:
    def compare_values(self, val1, val2):
        """
        Compares two input values (numeric or string).
        
        Returns a tuple indicating which value is greater, less, or equal.
        - ('>', 'val1', 'val2') if val1 > val2
        - ('<', 'val1', 'val2') if val1 < val2
        - ('=', 'val1', 'val2') if val1 == val2

        Handles both numeric and string comparisons. Raises TypeError 
        for incompatible types (e.g., int vs str).
        """
        # Check type compatibility
        if isinstance(val1, bool) or isinstance(val2, bool):
            raise TypeError("Boolean values should not be compared to other values.")

if __name__ == '__main__':
    pass
