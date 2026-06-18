class StringAssembler:
    """A class to efficiently construct strings from a list of parts."""
    
    def build(self, parts, separator):
        """
        Constructs a new string from the input list of parts and a chosen separator.
        
        Args:
            parts (list): A list of elements (strings or other types that can be converted to str).
            separator (str): The string to insert between each element in the result.
            
        Returns:
            str: The constructed string with separators placed between parts.
               If no parts are provided, returns an empty string.
               
        Examples:
            >>> assembler = StringAssembler()
            >>> assembler.build(["a", "b"], ",")
            'a,b'
        """
        # Handle edge case where list is None or not iterable effectively by converting to list first if needed,
        # though the signature implies a list. We use join which handles empty lists gracefully.
        return separator.join(str(part) for part in parts)

if __name__ == '__main__':
    assembler = StringAssembler()

    # Sample test cases without any user input or arguments
    
    # Test 1: Basic string joining
    result1 = assembler.build(["Hello", "World"], " ")
    
    # Test 2: Empty list handling
    result2 = assembler.build([], "-")
    
    # Test 3: Single element
    result3 = assembler.build(["OnlyOne"], "|")
    
    # Test 4: Mixed types (integers converted to strings)
    parts_mixed = [1, "two", 3.5]
    result4 = assembler.build(parts_mixed, ", ")

    print(f"Test 1 Result ('Hello', 'World' with space): '{result1}'")
    assert result1 == "Hello World"
    
    # Test 2 Check
    assert result2 == ""
    
    # Test 3 Check
    assert result3 == "OnlyOne"
    
    print(f"Test 4 Result (mixed types [1, 'two', 3.5] with ', '): '{result4}'")
    assert result4 == "1 two 3.5", f"Expected '1 two 3.5' but got {result4}"

    # Test 5: None separator handling (though task implies string) - strictly following type hint of str for sep usually, 
    # but we stick to basic usage as per common sense if not specified otherwise in docstring constraints beyond Args description.
    # Assuming standard behavior where separator is a string literal or variable passed correctly.

    print("All tests passed successfully.")