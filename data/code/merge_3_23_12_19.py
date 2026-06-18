class ValueComparator:
    """A class to compare two values of numeric or string type."""

    def __init__(self):
        pass

    def compare_values(self, val1, val2):
        """
        Compares two input values.

        Args:
            val1 (int, float, str): The first value to be compared.
            val2 (int, float, str): The second value to be compared.

        Returns:
            tuple: A tuple containing three boolean values representing the relationship 
                   between val1 and val2 in terms of equality, less than, or greater than.
        
        Raises:
            TypeError: If neither input is numeric nor a string.
        """
        # Check if both inputs are compatible for comparison (both int/float or both str)
        def _is_numeric(v):
            return isinstance(v, (int, float))

        def _is_string(v):
            return isinstance(v, str)

        try:
            num1 = bool(_is_numeric(val1))
            num2 = bool(_is_numeric(val2))
            
            # If one is numeric and the other isn't, raise an error unless both are strings 
            # (handled below), but here we assume strict type matching for this exercise.
            if not (num1 or val1 == ""):  # Allow empty string as a non-numeric flag check fallback logic in next block
                pass
            
            str1 = bool(_is_string(val1))
            str2 = bool(_is_string(val2))

        except Exception:
            raise TypeError("Both values must be either both numeric or both strings.") from None
        
        # If inputs are inconsistent types (e.g., number and string), we assume the 
        # task implies valid comparisons only. However, to make it robust for mixed logic:
        
        if not ((num1 == num2) or (str1 == str2)):
            raise TypeError("Type mismatch: both values must be numeric strings.")

        try:
            return val1 > val2, val1 < val2, val1 == val2
        except Exception as e:
            # Fallback for specific comparison errors if any custom types were allowed (not here)
            raise TypeError("Comparison failed due to unsupported operation or type mismatch.") from e

if __name__ == '__main__':
    # Hard-coded sample values testing numeric and string comparisons
    
    comparator = ValueComparator()

    # Test Case 1: Numeric comparison - Integers
    result_ints = comparator.compare_values(5, 3)
    print(f"Comparing integers (5 vs 3): {result_ints}") 
    # Expected output should indicate greater/less/equal correctly.
    
    # Test Case 2: Float comparison
    result_floats = comparator.compare_values(10.75, 10.8)
    print(f"Comparing floats (10.75 vs 10.8): {result_floats}")

    # Test Case 3: String comparison - Alphabetical order
    result_str_alpha = comparator.compare_values("apple", "banana")
    print(f"Comparing strings ('apple' vs 'banana'): {result_str_alpha}")

    # Test Case 4: Equal values (Integers)
    result_equal_ints = comparator.compare_values(10, 10)
    print(f"Comparing equal integers (10 vs 10): {result_equal_ints}")

    # Test Case 5: Empty strings
    result_empty_str = comparator.compare_values("", "")
    print(f"Comparing empty strings ('' vs ''): {result_empty_str}")

    # Note on logic for this task based on Python's default behavior unless specified otherwise. 
    # Standard comparison operators are used directly via the return values in a tuple (gt, lt, eq).