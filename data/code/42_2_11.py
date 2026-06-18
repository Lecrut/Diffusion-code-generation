class StringAssembler:
    def build(self, parts, separator):
        """
        Efficiently constructs a new string from a list of parts using a specified separator.
        
        Args:
            parts (list[str]): A list of strings to be joined.
            separator (str): The string used as the delimiter between elements in 'parts'.
            
        Returns:
            str: The constructed string with separators placed between each part.
        """
        if not parts:
            return ""
        
        # Using join is generally efficient for this task in Python, 
        # but we can optimize slightly by handling empty strings or None values if needed.
        # For standard use case where 'parts' contains valid strings and separator is a string:
        result = []
        for i, part in enumerate(parts):
            if not isinstance(part, str):
                raise TypeError(f"Expected all parts to be strings, got {type(part)} at index {i}")
            
            # Optimization: If the list is large, building a list of substrings and joining 
            # is faster than repeated concatenation. We do this here implicitly via join below.
            result.append(str(part))

        return separator.join(result)

if __name__ == '__main__':
    assembler = StringAssembler()
    
    sample_parts_1 = ["Hello", "World"]
    sample_separator_1 = ", "
    output_1 = assembler.build(sample_parts_1, sample_separator_1)
    print(f"Test 1: {output_1}")

    sample_parts_2 = ["Python", "is", "great", "!"]
    sample_separator_2 = "-"
    output_2 = assembler.build(sample_parts_2, sample_separator_2)
    print(f"Test 2: {output_2}")

    # Edge case with empty list
    sample_parts_empty = []
    separator_default = ""
    output_empty = assembler.build(sample_parts_empty, separator_default)
    print(f"Empty List Test: '{output_empty}'")