class StringAssembler:
    """A utility class to efficiently construct strings from a list of parts."""
    
    def build(self, parts, separator):
        """
        Constructs a new string by joining all elements in 'parts' with the specified 'separator'.
        
        Args:
            parts (list[str]): A list containing zero or more strings.
            separator (str): The string to use as the delimiter between items.
            
        Returns:
            str: The resulting joined string. If 'parts' is empty, returns an empty string.
        """
        return "".join(parts) if not parts else separator.join(str(p) for p in parts)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    assembler = StringAssembler()
    
    # Test case 1: Normal list of strings with a standard separator
    result1 = assembler.build(["Hello", " ", "World"], "")
    print(f"Test 1 (Empty Separator): '{result1}'")

    # Test case 2: List with custom separator and mixed types converted to string internally logic handled by generator
    parts2 = [1, "two", 3.0] 
    result2 = assembler.build(parts2, ", ")
    print(f"Test 2 (Custom Separator): '{result2}'")

    # Test case 3: Empty list handling
    result3 = assembler.build([], "-")
    print(f"Test 3 (Empty List): '{result3}'")
    
    # Verification
    assert result1 == "Hello World", f"Expected 'Hello World', got {result1}"
    assert result2 == "1, two, 3.0", f"Expected '1, two, 3.0', got {result2}"
    assert result3 == "", f"Expected empty string, got '{result3}'"

    print("All tests passed successfully.")