class ValueComparator:
    def compare_values(self, val1, val2):
        """
        Compares two input values (numeric or string) and returns a tuple indicating
        which value is greater, less, or equal.
        
        Returns one of the following tuples:
            ('>', 'val1', 'val2') if val1 > val2
            ('<', 'val1', 'val2') if val1 < val2
            ('=', 'val1', 'val2') otherwise
        
        Supports comparison between numbers, strings, and mixed types where applicable.
        """
        try:
            # Attempt numeric conversion for both values to allow number vs string comparisons (e.g., "3" > 2)
            num_val1 = float(val1) if not isinstance(val1, (int, float)) else val1
            num_val2 = float(val2) if not isinstance(val2, (int, float)) else val2
            
            # If both are valid numbers, compare numerically
            if isinstance(num_val1, (int, float)) and isinstance(num_val2, (int, float)):
                comparison_type = '>' if num_val1 > num_val2 else ('<' if num_val1 < num_val2 else '=')
                return (comparison_type, val1, val2)
        except (ValueError, TypeError):
            pass
        
        # Fallback to string comparison if numeric conversion fails or types are strings only
        try:
            str_comparison = '>' if str(val1) > str(val2) else ('<' if str(val1) < str(val2) else '=')
            return (str_comparison, val1, val2)
        except TypeError:
            # If neither numeric nor string comparison works directly due to type mismatch issues not covered above,
            # we prioritize the first successful check. Since this block is reached only if previous attempts failed,
            # it implies a complex mixed case where standard Python comparisons might have been attempted implicitly 
            # by Python's duck typing in some contexts, but explicit float conversion was tried.
            # As a final safety net for any remaining edge cases that are technically comparable:
            try:
                comparison_type = '>' if val1 > val2 else ('<' if val1 < val2 else '=')
                return (comparison_type, val1, val2)
            except TypeError:
                # Absolute fallback returning equality or a default indicator based on identity 
                # though logically this should not be reached for valid inputs.
                return ('=', val1, val2)

if __name__ == '__main__':
    comparator = ValueComparator()

    test_cases = [
        (5, 3),           # Numeric: >
        ("apple", "banana"),   # String: <
        (4.5, 4.5),       # Equal numeric
        ("10", 2),         # Mixed string/number comparison as strings usually ('10' < '2') but numerically 10>2. 
                          # Based on docstring logic above: tries float conversion first -> "10" becomes 10.0, 2 is int -> compares numbers (>)
        ("hello", "world"),   # String >
        (-1, -5),          # Numeric <
    ]

    print("Value Comparison Results:")
    for val1, val2 in test_cases:
        result = comparator.compare_values(val1, val2)
        op, v1, v2 = result
        print(f"Comparing {repr(v1)} and {repr(v2)} -> Result: {op}")