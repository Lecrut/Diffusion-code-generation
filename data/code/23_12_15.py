class ValueComparator:
    def compare_values(self, val1, val2):
        """
        Compares two input values (numeric or string) and returns a tuple indicating their relationship.
        
        Args:
            val1 (int, float, str): The first value to compare.
            val2 (int, float, str): The second value to compare.
            
        Returns:
            tuple: A single-element tuple containing the result string ('>', '<', or '=').
                   If types are incompatible for comparison without conversion errors, it handles them gracefully 
                   by attempting type coercion if possible (e.g., int/float vs str representing numbers), otherwise 
                   falls back to direct comparison rules where applicable.
        """
        try:
            # Attempt numeric conversion if one is string and the other is number-like
            def make_numeric(v):
                return float(str(v))

            num1, num2 = None, None
            
            if isinstance(val1, str) or isinstance(val2, str):
                # Try to convert strings to numbers for comparison
                try:
                    val1_num = float(val1)
                    val2_num = float(val2)
                    return ('>', '<', '=')[val1_num > val2_num] if (val1_num != val2_num) else '='
                except ValueError:
                    # If conversion fails, treat as strings and compare alphabetically/lexicographically
                    pass
            
            try:
                result = '>' if val1 > val2 else ('<' if val1 < val2 else '=')
                return (result,)
            except TypeError:
                # Fallback for completely incompatible types not covered above, 
                # though standard Python handles most mixed type comparisons by promoting to common base.
                pass
                
        except Exception:
            # In case of any unexpected error during comparison logic
            return ('=',)

if __name__ == '__main__':
    comp = ValueComparator()
    
    test_cases = [
        (10, 5),           # Integers
        (3.5, 2.7),       # Floats
        ("apple", "banana"),      # Strings
        (42, "99"),              # Mixed numeric/string that can be converted to float
        (-5, -10),         # Negative integers
    ]

    for val1, val2 in test_cases:
        result = comp.compare_values(val1, val2)
        print(f"Comparing {val1} and {val2}: Result is {result[0]}")