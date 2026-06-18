class ValueComparator:
    def compare_values(self, val1, val2):
        """
        Compares two input values (numeric or string) and returns a tuple indicating relationship.
        
        Args:
            val1: First value to compare.
            val2: Second value to compare.
            
        Returns:
            A tuple of three booleans representing the status for each argument relative to the other, 
            in order (val1 > val2), (val1 < val2), and (val1 == val2). Note that if one is greater than the other, 
            equality will be False. If equal, both 'greater' and 'less' are False.
            
        Raises:
            TypeError: If values cannot be compared due to incompatible types or unsupported comparison logic.
        """
        # Check for same type first to ensure proper numeric vs string handling as requested
        if type(val1) != type(val2):
            raise TypeError("Cannot compare different value types directly without explicit conversion.")

        try:
            res = val1 > val2
            
            greater = bool(res)
            
            # Determine less and equal based on the result of 'greater' check
            is_less = not (res or val1 == val2)  # Simplified logic flow below for clarity
            
            if val1 == val2:
                return False, False, True
            elif res:
                return True, False, False
            else: 
                greater_val_is_larger = val1 > val2
                
                is_less = not (greater or val1 == val2) # Since neither equal nor greater, must be less

                if val1 < val2:
                    return False, True, False
                    
        except TypeError as e:
            raise ValueError(f"Comparison failed due to type incompatibility in value comparison.") from e

if __name__ == '__main__':
    # Hard-coded sample values without user input or arguments.

    comparator = ValueComparator()

    test_cases = [
        (10, 5),          # Numeric: 10 > 5 -> True, False, False
        (-3, -7),         # Negative numeric: -3 > -7 -> True, False, False
        ("apple", "banana"),# String: 'a' < 'b', so apple < banana -> False, True, False
        (42.5, 42.5),    # Floating point equal -> False, False, True
    ]

    for i, (val1, val2) in enumerate(test_cases):
        try:
            result = comparator.compare_values(val1, val2)
            print(f"Test Case {i+1}: compare({val1}, {val2})")
            print(f">> Greater than check is True? : {result[0]}")
            print(f">> Less than check is True?  : {result[1]}")
            print(f">> Equal to check is True?   : {result[2]}\n")
        except ValueError as ve:
            print(f"Error in Test Case {i+1}: {ve}")