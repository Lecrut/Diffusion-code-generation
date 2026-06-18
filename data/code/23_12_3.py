class ValueComparator:
    def compare_values(self, val1, val2):
        """
        Compares two input values (numeric or string) and returns a tuple indicating 
        which value is greater, less than, or equal to the other.
        
        Args:
            val1: First value to compare. Can be int, float, str, etc.
            val2: Second value to compare. Should match type of val1 for consistent comparison.
            
        Returns:
            A tuple (result_type, greater_value) where result_type is 'greater', 
            'less' or 'equal'. If types differ significantly and cannot be compared directly,
            a TypeError will be raised unless both are strings.
        """
        
        # Attempt to compare as numbers first if possible
        try:
            num1 = float(val1)
            num2 = float(val2)
            
            if val1 == val2:
                return ('equal', val1)
            elif num1 > num2:
                return ('greater', val1)
            else:
                return ('less', val2)
        except (ValueError, TypeError):
            pass
        
        # If numeric comparison failed or values are strings, compare as strings
        try:
            str_val1 = str(val1).lower()
            str_val2 = str(val2).lower()
            
            if str_val1 == str_val2:
                return ('equal', val1)
            elif str_val1 > str_val2:
                return ('greater', val1)
            else:
                return ('less', val2)
        except Exception:
            # If all comparisons fail, raise an error indicating incompatible types
            raise TypeError(f"Cannot compare values of type {type(val1)} and {type(val2)}. "
                           f"Provide numeric or string-compatible inputs.")

if __name__ == '__main__':
    comparator = ValueComparator()
    
    # Sample test cases with hard-coded values
    
    # Test 1: Numeric comparison (integers)
    result_ints = comparator.compare_values(10, 5)
    print(f"Integers (10 vs 5): {result_ints}")
    
    # Test 2: Floating point numbers
    result_floats = comparator.compare_values(3.14, 2.71)
    print(f"Floats (3.14 vs 2.71): {result_floats}")
    
    # Test 3: Equal integers
    result_equal_ints = comparator.compare_values(50, 50)
    print(f"Equal Integers (50 vs 50): {result_equal_ints}")
    
    # Test 4: String comparison
    result_strings = comparator.compare_values("zebra", "apple")
    print(f"Strings ('zebra' vs 'apple'): {result_strings}")
    
    # Test 5: Equal strings (case insensitive)
    result_case_insensitive = comparator.compare_values("Hello", "hello")
    print(f"Case-insensitive Strings ('Hello' vs 'hello'): {result_case_insensitive}")
    
    # Test 6: Mixed types that convert to numbers successfully
    result_mixed_numeric = comparator.compare_values(10.5, "20")
    print(f"Mixed Numeric (" + str(result_mixed_numeric) + ")")