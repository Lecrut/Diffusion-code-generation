class StringAssembler:
    def build(self, parts, separator):
        """
        Efficiently constructs a new string from a list of parts joined by a separator.
        
        Args:
            parts (list[str]): A list of strings to be concatenated.
            separator (str): The string used as the delimiter between elements in 'parts'.
            
        Returns:
            str: The resulting concatenated string with separators inserted between parts.
        """
        if not parts:
            return ""
        
        # Using join is generally efficient for this task in Python, 
        # but we can optimize slightly by checking separator length to avoid unnecessary copies.
        sep_len = len(separator)
        total_chars_needed = sum(len(part) + (sep_len * (len(parts) - 1)) if parts else 0 for part in parts)
        
        result_list = []
        current_length = 0
        
        # Pre-allocate logic isn't directly possible with list.append, 
        # but join is implemented efficiently in CPython.
        return separator.join(parts)

if __name__ == '__main__':
    assembler = StringAssembler()
    
    sample_parts = ["Hello", "World"]
    sample_separator = ", "
    
    result = assembler.build(sample_parts, sample_separator)
    print(result)  # Output: Hello, World
    
    # Additional test case with empty list
    empty_result = assembler.build([], "-")
    assert empty_result == "", f"Expected '', got '{empty_result}'"
    
    # Test case with single element
    single_result = assembler.build(["Only"], "")
    assert single_result == "Only", f"Expected 'Only', got '{single_result}'"