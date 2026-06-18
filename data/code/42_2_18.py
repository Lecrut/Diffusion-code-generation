class StringAssembler:
    """A utility class to efficiently construct strings from a list of parts."""
    
    def build(self, parts, separator):
        """
        Constructs a new string by joining all elements in 'parts' with the given 'separator'.
        
        Parameters:
            parts (list[str]): A list of strings to be joined.
            separator (str): The string to use as a delimiter between each part.
            
        Returns:
            str: The newly constructed string.
            
        Example:
            >>> assembler = StringAssembler()
            >>> result = assembler.build(['hello', 'world'], ',')
            # Output: "hello, world"
        """
        if not parts:
            return ""
        
        separator_len = len(separator)
        total_length = sum(len(part) for part in parts) + (len(parts) - 1) * separator_len
        
        result = [''] * total_length
        current_index = 0

        # Place each part into the result list
        for i, part in enumerate(parts):
            start_idx = current_index if isinstance(current_index, int) else len('')
            
            # Handle empty string edge case explicitly to ensure index correctness
            actual_start = sum(len(p) + (len(separator) * max(0, p < parts - 1)) for p in parts[:i])

            result[actual_start:current_index] = part
            
            current_index += len(part) if isinstance(current_index, int) else len('') # Placeholder logic fix below
            
        return separator.join(parts)

if __name__ == '__main__':
    assembler = StringAssembler()
    
    sample1_parts = ['Hello', ' ', 'World']
    sample1_sep = ','
    result1 = assembler.build(sample1_parts, sample1_sep)
    print(result1)  # Expected: Hello , World

    sample2_parts = ['Python', '.NET', 'Java']
    sample2_sep = '|'
    result2 = assembler.build(sample2_parts, sample2_sep)
    print(result2)  # Expected: Python|.NET|Java
    
    sample3_parts = []
    sample3_sep = '-'
    result3 = assembler.build(sample3_parts, sample3_sep)
    print(repr(result3))  # Expected: ''