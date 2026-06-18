class ValueComparator:
    def compare(self, val1, val2):
        """
        Compares two input values of comparable types (e.g., int, float, str).
        
        Args:
            val1: The first value to compare.
            val2: The second value to compare.
            
        Returns:
            A string indicating the result of comparison:
            - "val1 is greater than val2" if val1 > val2
            - "val2 is greater than val1" if val2 > val1
            - "values are equal" otherwise
            
        Raises:
            TypeError: If the values cannot be compared.
            
        Example:
            >>> comparator = ValueComparator()
            >>> result = comparator.compare(3, 5)
            print(result) # Output: 5 is greater than 3
        """
        try:
            if val1 > val2:
                return f"{val1} is greater than {val2}"
            elif val2 > val1:
                return f"{val2} is greater than {val1}"
            else:
                return "values are equal"
        except TypeError as e:
            raise TypeError(f"Incompatible types for comparison, got '{type(val1).__name__}' and '{type(val2).__name__}'.") from e

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    
    # Test 1: Integer comparison (val1 > val2)
    comp = ValueComparator()
    result1 = comp.compare(5, 3)
    print(f"Test 1 - Integers: {result1}")

    # Test 2: Float comparison (equal)
    result2 = comp.compare(4.5, 4.5)
    print(f"Test 2 - Floats equal: {result2}")

    # Test 3: String comparison
    result3 = comp.compare("apple", "banana")
    print(f"Test 3 - Strings: {result3}")

    # Test 4: Reverse integer comparison (val1 < val2)
    result4 = comp.compare(9, 8765)
    print(f"Test 4 - Integers reverse: {result4}")

    # Output verification (no user input required to run):
    # Expected output lines will match the comments in the script above.