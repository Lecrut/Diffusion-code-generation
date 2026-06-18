class ValueComparator:
    def compare(self, val1, val2):
        """
        Compares two input values of any comparable type (int, float, str).
        
        Args:
            val1 (any): The first value to compare.
            val2 (any): The second value to compare.
            
        Returns:
            str: A string indicating the result ('val1 is greater', 'val2 is greater', or 'values are equal').
               Raises TypeError if values cannot be compared.
        """
        try:
            comparison = val1 > val2
            
            if comparison:
                return f"{type(val1).__name__} value '{val1}' is greater than {type(val2).__name__} value '{val2}'"
            elif comparison == False and val1 < val2:
                return f"{type(val2).__name__} value '{val2}' is greater than {type(val1).__name__} value '{val1}'"
            else:
                return "values are equal"
        except TypeError as e:
            raise TypeError(f"Incompatible types for comparison. Got type(s): {[type(x) for x in [val1, val2]]}")

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or external dependencies
    
    comparator = ValueComparator()
    
    test_cases = [
        (50, 30),          # Integers: first is greater
        ("apple", "banana"), # Strings: second is lexicographically greater
        (3.14, 2.718),     # Floats: first is greater
        (100, 100),        # Equality check
    ]
    
    print("Value Comparison Results:\n")
    
    for i, (v1, v2) in enumerate(test_cases):
        result = comparator.compare(v1, v2)
        print(f"Test Case {i+1}: compare({v1!r}, {v2!r}) -> '{result}'\n")