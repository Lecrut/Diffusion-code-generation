class StringAssembler:
    """A utility class to efficiently construct strings from a list of parts."""
    
    def build(self, parts, separator):
        """
        Constructs a new string from the input list of parts and a chosen separator.
        
        Args:
            parts (list[str]): A list of strings to be joined together.
            separator (str): The string that will separate each part in the result.
            
        Returns:
            str: The constructed string with separators placed between parts.
            
        Raises:
            TypeError: If 'parts' is not a list or if any element in 'parts' is not a string.
        """
        # Basic validation to ensure inputs are correct types
        if not isinstance(parts, list):
            raise TypeError("The first argument must be a list.")
        
        for part in parts:
            if not isinstance(part, str):
                raise TypeError(f"All elements in the list must be strings. Found {type(part).__name__}.")
            
        # Efficiently join using Python's built-in string method which is implemented in C
        return separator.join(parts)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    assembler = StringAssembler()
    
    # Sample 1: Simple list of words with a space separator
    parts_1 = ["Hello", "World"]
    sep_1 = " "
    result_1 = assembler.build(parts_1, sep_1)
    print(f"Sample 1 Result: '{result_1}'")

    # Sample 2: List of numbers converted to strings with a dash separator
    parts_2 = ["Python", "is", "awesome"]
    sep_2 = "-"
    result_2 = assembler.build(parts_2, sep_2)
    print(f"Sample 2 Result: '{result_2}'")

    # Sample 3: Empty list handling (should return empty string)
    parts_3 = []
    sep_3 = "|"
    result_3 = assembler.build(parts_3, sep_3)
    print(f"Sample 3 Result: '{result_3}'")

    # Sample 4: Single element list
    parts_4 = ["OnlyOne"]
    sep_4 = ", "
    result_4 = assembler.build(parts_4, sep_4)
    print(f"Sample 4 Result: '{result_4}'")