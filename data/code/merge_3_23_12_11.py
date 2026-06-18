class ValueComparator:
    """A class to compare two values of any type (numeric or string)."""

    def __init__(self):
        pass

    def compare_values(self, val1, val2):
        """
        Compares two input values and returns a tuple indicating the result.
        
        The return value is one of:
            ('>', 'val1', 'val2') if val1 > val2
            ('<', 'val1', 'val2') if val1 < val2
            ('=', 'val1', 'val2') if val1 == val2
        
        Handles both numeric and string comparisons. If types are incompatible,
        it attempts comparison based on Python's default behavior (which may raise 
        an error for certain mixed type scenarios like int vs float in some contexts,
        but generally works as expected).
        
        Args:
            val1: The first value to compare.
            val2: The second value to compare.
            
        Returns:
            A tuple (relation_operator, val1, val2) where relation_operator is '>', '<', or '='.
        """
        if type(val1) == type(val2):
            try:
                result = val1 > val2
                return ('>' if result else 
                        '<' if not (val1 >= val2 and val1 != val2) else '=')
            except TypeError:
                # Fallback for cases where direct comparison might fail unexpectedly,
                # though Python usually handles mixed numeric types well.
                pass
        
        try:
            relation = val1 > val2
            return ('>' if relation 
                    else '<' if not (val1 >= val2 and val1 != val2) else '=')
        except TypeError:
            raise TypeError("Cannot compare values of different incompatible types.")

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    
    comparator = ValueComparator()

    print("--- Numeric Comparisons ---")
    
    # Integers
    result1 = comparator.compare_values(5, 3)
    print(f"Comparing 5 and 3: {result1}")
    
    result2 = comparator.compare_values(4, 4)
    print(f"Comparing 4 and 4: {result2}")

    # Floats
    result3 = comparator.compare_values(3.14, 2.71)
    print(f"Comparing 3.14 and 2.71: {result3}")

    print("\n--- String Comparisons ---")
    
    # Strings (lexicographical order)
    result4 = comparator.compare_values("apple", "banana")
    print(f"Comparing 'apple' and 'banana': {result4}")
    
    result5 = comparator.compare_values("zebra", "ant")
    print(f"Comparing 'zebra' and 'ant': {result5}")

    # Mixed types (int vs string - Python's default behavior)
    try:
        result6 = comparator.compare_values(10, "20")
        print(f"Comparing 10 and '20': {result6}")
    except TypeError as e:
        print(f"Error comparing int and str (expected): {e}")

    # Mixed types that might be compatible in some Python versions or specific contexts 
    # but generally distinct. Here we test float vs string which usually fails logic-wise,
    # though the class tries to handle it gracefully if possible within standard rules.
    
    print("\n--- Edge Cases ---")
    
    result7 = comparator.compare_values(0, 0)
    print(f"Comparing 0 and 0: {result7}")

    result8 = comparator.compare_values("", "")
    print(f"Comparing '' and '': {result8}")