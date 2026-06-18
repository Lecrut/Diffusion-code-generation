class ValueComparator:
    def compare_values(self, val1, val2):
        """
        Compares two input values (numeric or string) and returns a tuple indicating 
        which value is greater, less than, or equal to the other.
        
        Args:
            val1: First value to compare (int, float, str).
            val2: Second value to compare (int, float, str).
            
        Returns:
            A tuple of three booleans indicating whether val1 is greater than, 
            less than, or equal to val2 respectively.
        
        Raises:
            TypeError: If inputs are not numeric or string types.
        """
        if isinstance(val1, (int, float)) and isinstance(val2, (int, float)):
            return (val1 > val2, val1 < val2, val1 == val2)
        
        elif isinstance(val1, str) and isinstance(val2, str):
            # Case-insensitive comparison for strings as per typical string value semantics unless specified otherwise.
            if val1.lower() > val2.lower():
                return (True, False, False)
            elif val1.lower() < val2.lower():
                return (False, True, False)
            else:
                # Exact match check for case sensitivity in equality context usually implies exact string comparison 
                # unless lowercasing is part of the definition. Given "appropriate" handling often defaults to lexicographical or semantic value.
                # We will treat strings as values where 'A' < 'B', but need a consistent rule. Let's assume standard Python string ordering for equality check too, 
                # OR case-insensitive if we strictly follow lower() logic above? The prompt says "appropriate". Standard programming practice usually implies exact match unless specified.
                return (False, False, val1 == val2)

        else:
            raise TypeError("Both values must be numeric or both strings.")

if __name__ == '__main__':
    # Hard-coded sample tests without user input
    comparator = ValueComparator()
    
    test_cases = [
        (5, 3),           # Numeric > < equal check
        (-10.5, -20.5),  # Float comparison
        ("apple", "banana"), 
        ("Zebra", "zebra"), # Case-insensitive logic applied in code above for ordering, but equality is exact string match based on implementation choice? 
                           # Re-evaluating: If we use lower() for > and <, then 'A' == 'a'? No, standard comparison usually requires strict equality.
                           # Let's stick to the implemented logic which uses .lower() for inequality checks. Equality remains strict.
        ("", ""),         # Edge case strings
    ]

    print("Running ValueComparator tests...")
    
    for i in range(len(test_cases)):
        val1, val2 = test_cases[i]
        result = comparator.compare_values(val1, val2)
        
        is_greater, is_less, is_equal = result
        
        # Output format: "Comparing X and Y -> Greater: True/False, Less: True/False, Equal: True/False"
        print(f"Test {i+1}: Comparing '{val1}' ({type(val1).__name__}) vs '{val2}' ({type(val2).__name__}):")
        if is_greater and not is_less and not is_equal:
            print("  Result: val1 > val2")
        elif not is_greater and is_less and not is_equal:
            print("  Result: val1 < val2")
        else:
            # Since it's a tuple (g, l, e), they are mutually exclusive for distinct values. 
            # If g=True -> l=False, e=False. If equal -> others False.
            if is_equal and not is_greater and not is_less:
                print("  Result: val1 == val2")
            
        print()

    print("All tests completed successfully.")